from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
from uuid import uuid4
from datetime import datetime

try:
    # Подключение к кластеру
    cluster = Cluster(['cassandra1'], port=9042)
    session = cluster.connect()
    print("Подключение успешно")
    # 1. Создание keyspace
    # ToDO будет использована стратегия где данные реплицируются на 3 разных узлах
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS my_keyspace 
        WITH replication = {
            'class': 'SimpleStrategy',
            'replication_factor': 3
        }
    """)
    session.set_keyspace('my_keyspace')

    # 2. Создание таблиц
    # Таблица 1: с составным Partition key (customer_id, order_id) - всегда идет на первом месте и Clustering key = order_date,
    # все поля, которые перечисляются после Partition key являются clustering key
    session.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            customer_id uuid,
            order_id uuid,
            order_date timestamp,
            product_name text,
            price decimal,
            status text,
            PRIMARY KEY ((customer_id, order_id), order_date)
        ) WITH CLUSTERING ORDER BY (order_date DESC)
    """)

    # Таблица 2: стандартная
    session.execute("""
        CREATE TABLE IF NOT EXISTS products (
            product_id uuid PRIMARY KEY,
            name text,
            category text,
            price decimal,
            stock int
        )
    """)

    # 3. Заполнение данными
    # Заполнение orders
    orders_data = [
        (uuid4(), uuid4(), datetime.now(), 'Laptop', 999.99, 'completed'),
        (uuid4(), uuid4(), datetime.now(), 'Smartphone', 699.99, 'processing'),
        (uuid4(), uuid4(), datetime.now(), 'Headphones', 149.99, 'shipped')
    ]

    insert_order = session.prepare("""
        INSERT INTO orders (customer_id, order_id, order_date, product_name, price, status)
        VALUES (?, ?, ?, ?, ?, ?)
    """)

    for order in orders_data:
        session.execute(insert_order, order)

    # Заполнение products
    products_data = [
        (uuid4(), 'Laptop', 'Electronics', 999.99, 10),
        (uuid4(), 'Smartphone', 'Electronics', 699.99, 15),
        (uuid4(), 'Desk Chair', 'Furniture', 199.99, 5)
    ]

    insert_product = session.prepare("""
        INSERT INTO products (product_id, name, category, price, stock)
        VALUES (?, ?, ?, ?, ?)
    """)

    for product in products_data:
        session.execute(insert_product, product)

    # 4. Выполнение запросов с WHERE
    print("\nЗапрос 1: Заказы конкретного клиента")
    customer_id = orders_data[0][0]
    rows = session.execute("""
        SELECT * FROM orders 
        WHERE customer_id = %s ALLOW FILTERING
    """, [customer_id])
    for row in rows:
        print(row)

    print("\nЗапрос 2: Товары в категории Electronics")
    rows = session.execute("""
        SELECT * FROM products 
        WHERE category = 'Electronics' ALLOW FILTERING
    """)
    for row in rows:
        print(row)

    print("\nЗапрос 3: Заказы дороже 500")
    rows = session.execute("""
        SELECT * FROM orders 
        WHERE price > 500 ALLOW FILTERING
    """)
    for row in rows:
        print(row)

    # 5. Создание вторичного индекса
    session.execute("""
        CREATE INDEX IF NOT EXISTS ON orders (status)
    """)

    print("\nЗапрос 4: Заказы со статусом 'processing' (используя вторичный индекс)")
    rows = session.execute("""
        SELECT * FROM orders WHERE status = 'processing'
    """)
    for row in rows:
        print(row)


    # 6. Нагрузочное тестирование (опционально)
    def run_stress_test():
        print("\nЗапуск Cassandra Stress Tool...")
        # Для выполнения stress-теста нужно использовать отдельную команду
        # Пример команды (выполняется в терминале, не в Python):
        # cassandra-stress write n=100000 cl=one -mode native cql3 -schema keyspace=my_keyspace -node localhost

        print("""
        Чтобы выполнить нагрузочное тестирование, запустите в терминале:
        cassandra-stress write n=100000 cl=one -mode native cql3 -schema keyspace=my_keyspace -node localhost
        Или используйте конфигурационный файл для более сложных тестов.
        """)


    # Раскомментируйте для запуска теста
    # run_stress_test()

    # Закрытие соединения
    cluster.shutdown()
except Exception as e:
    print("Не удалось подключиться", e)


