## Использование

1. Запустите сервисы:
   ```bash
   docker-compose up -d
   ```
   
2. Проверьте статус результатов
   ```bash
   docker exec -it cassandra1 nodetool status
   ```
3. Запустите 
   ```bash
   docker-compose exec python-app python /app/cassandra_cluster.py
   ```
   или прям из конейнера
   ```bash
   docker-compose run --rm python-app bash
   ```
   а затем
   ```bash
   python /app/cassandra_cluster.py

## Результаты работы скрипта cassandra_cluster.py
```txt
Запрос 1: Заказы конкретного клиента
Row(customer_id=UUID('d165c222-6fac-4d51-87f5-fd4a30766a17'), order_id=UUID('8e213689-2716-4673-a540-83aadda5e4e6'), order_date=datetime.datetime(2025, 4, 21, 15, 36, 24, 432000), price=Decimal('999.990000000000009094947017729282379150390625'), product_name='Laptop', status='completed')

Запрос 2: Товары в категории Electronics
Row(product_id=UUID('f7d19690-2d05-462c-bd5c-3a5384430bc1'), category='Electronics', name='Smartphone', price=Decimal('699.990000000000009094947017729282379150390625'), stock=15)
Row(product_id=UUID('85bd3e05-7a68-4bee-a221-88389be1255a'), category='Electronics', name='Smartphone', price=Decimal('699.990000000000009094947017729282379150390625'), stock=15)
Row(product_id=UUID('892aa654-bdcd-4c05-8242-a8e54ae0a871'), category='Electronics', name='Smartphone', price=Decimal('699.990000000000009094947017729282379150390625'), stock=15)
Row(product_id=UUID('8c01ceb3-cef3-4ffa-aa00-ae9a9108d49c'), category='Electronics', name='Laptop', price=Decimal('999.990000000000009094947017729282379150390625'), stock=10)
Row(product_id=UUID('93a68c11-5502-480e-9434-2c56666ba204'), category='Electronics', name='Laptop', price=Decimal('999.990000000000009094947017729282379150390625'), stock=10)
Row(product_id=UUID('652633ae-bea5-4b46-a575-867ee475aacc'), category='Electronics', name='Laptop', price=Decimal('999.990000000000009094947017729282379150390625'), stock=10)

Запрос 3: Заказы дороже 500
Row(customer_id=UUID('25d25ffa-10f3-4521-85fc-fdbbcb5866fb'), order_id=UUID('d3218026-f0ea-4dc6-87d7-e4168686258c'), order_date=datetime.datetime(2025, 4, 20, 15, 40, 31, 247000), price=Decimal('699.990000000000009094947017729282379150390625'), product_name='Smartphone', status='processing')
Row(customer_id=UUID('c450a202-b524-49eb-84ff-9d65157987b1'), order_id=UUID('7c81bb43-1547-4fc1-af84-54ee2ff38852'), order_date=datetime.datetime(2025, 4, 21, 15, 5, 8, 611000), price=Decimal('999.990000000000009094947017729282379150390625'), product_name='Laptop', status='completed')
Row(customer_id=UUID('7b39994b-a1dc-4658-af96-b941b4009451'), order_id=UUID('b35053a4-ab9e-41b5-b754-7089385ab3f5'), order_date=datetime.datetime(2025, 4, 21, 15, 36, 24, 432000), price=Decimal('699.990000000000009094947017729282379150390625'), product_name='Smartphone', status='processing')
Row(customer_id=UUID('ccc45972-d8e7-467e-9691-b8ad1043f47c'), order_id=UUID('6b644688-b6db-4a72-b6aa-fb6425a5e5e5'), order_date=datetime.datetime(2025, 4, 21, 15, 5, 8, 611000), price=Decimal('699.990000000000009094947017729282379150390625'), product_name='Smartphone', status='processing')
Row(customer_id=UUID('9c22477e-08b3-43dc-b91c-442eb3731461'), order_id=UUID('58761314-2ea1-4b87-b7ee-e5c52c240f04'), order_date=datetime.datetime(2025, 4, 20, 15, 40, 31, 247000), price=Decimal('999.990000000000009094947017729282379150390625'), product_name='Laptop', status='completed')
Row(customer_id=UUID('d165c222-6fac-4d51-87f5-fd4a30766a17'), order_id=UUID('8e213689-2716-4673-a540-83aadda5e4e6'), order_date=datetime.datetime(2025, 4, 21, 15, 36, 24, 432000), price=Decimal('999.990000000000009094947017729282379150390625'), product_name='Laptop', status='completed')

Запрос 4: Заказы со статусом 'processing' (используя вторичный индекс)
Row(customer_id=UUID('25d25ffa-10f3-4521-85fc-fdbbcb5866fb'), order_id=UUID('d3218026-f0ea-4dc6-87d7-e4168686258c'), order_date=datetime.datetime(2025, 4, 20, 15, 40, 31, 247000), price=Decimal('699.990000000000009094947017729282379150390625'), product_name='Smartphone', status='processing')
Row(customer_id=UUID('7b39994b-a1dc-4658-af96-b941b4009451'), order_id=UUID('b35053a4-ab9e-41b5-b754-7089385ab3f5'), order_date=datetime.datetime(2025, 4, 21, 15, 36, 24, 432000), price=Decimal('699.990000000000009094947017729282379150390625'), product_name='Smartphone', status='processing')
Row(customer_id=UUID('ccc45972-d8e7-467e-9691-b8ad1043f47c'), order_id=UUID('6b644688-b6db-4a72-b6aa-fb6425a5e5e5'), order_date=datetime.datetime(2025, 4, 21, 15, 5, 8, 611000), price=Decimal('699.990000000000009094947017729282379150390625'), product_name='Smartphone', status='processing')
```


## Нагрузочное тестирование
```bash
docker exec -it cassandra1 /opt/cassandra/tools/bin/cassandra-stress write n=100000 -node cassandra1,cassandra2,cassandra3
```

```txt
C:\Users\chess\OtusNoSQl\casandra>docker exec -it cassandra1 /opt/cassandra/tools/bin/cassandra-stress write n=100000 -node cassandra1,cassandra2,cassandra3
******************** Stress Settings ********************
Command:
  Type: write
  Count: 100,000
  No Warmup: false
  Consistency Level: LOCAL_ONE
  Target Uncertainty: not applicable
  Key Size (bytes): 10
  Counter Increment Distibution: add=fixed(1)
Rate:
  Auto: false
  Thread Count: 200
  OpsPer Sec: 0
Population:
  Sequence: 1..100000
  Order: ARBITRARY
  Wrap: true
Insert:
  Revisits: Uniform:  min=1,max=1000000
  Visits: Fixed:  key=1
  Row Population Ratio: Ratio: divisor=1.000000;delegate=Fixed:  key=1
  Batch Type: not batching
Columns:
  Max Columns Per Key: 5
  Column Names: [C0, C1, C2, C3, C4]
  Comparator: AsciiType
  Timestamp: null
  Variable Column Count: false
  Slice: false
  Size Distribution: Fixed:  key=34
  Count Distribution: Fixed:  key=5
Errors:
  Ignore: false
  Tries: 10
Log:
  No Summary: false
  No Settings: false
  File: null
  Interval Millis: 1000
  Level: NORMAL
Mode:
  API: JAVA_DRIVER_NATIVE
  Connection Style: CQL_PREPARED
  CQL Version: CQL3
  Protocol Version: V5
  Username: null
  Password: null
  Auth Provide Class: null
  Max Pending Per Connection: 128
  Connections Per Host: 8
  Compression: NONE
Node:
  Nodes: [cassandra1, cassandra2, cassandra3]
  Is White List: false
  Datacenter: null
Schema:
  Keyspace: keyspace1
  Replication Strategy: org.apache.cassandra.locator.SimpleStrategy
  Replication Strategy Options: {replication_factor=1}
  Table Compression: null
  Table Compaction Strategy: null
  Table Compaction Strategy Options: {}
Transport:
  truststore=null; truststore-password=null; keystore=null; keystore-password=null; ssl-protocol=TLS; ssl-alg=null; ssl-ciphers=TLS_RSA_WITH_AES_128_CBC_SHA,TLS_RSA_WITH_AES_256_CBC_SHA;
Port:
  Native Port: 9042
  JMX Port: 7199
Graph:
  File: null
  Revision: unknown
  Title: null
  Operation: WRITE
TokenRange:
  Wrap: false
  Split Factor: 1

Connected to cluster: MyCluster, max pending requests per connection 128, max connections per host 8
Datacenter: datacenter1; Host: cassandra3/172.18.0.4:9042; Rack: rack1
Datacenter: datacenter1; Host: cassandra1/172.18.0.2:9042; Rack: rack1
Datacenter: datacenter1; Host: cassandra2/172.18.0.3:9042; Rack: rack1
Created keyspaces. Sleeping 3s for propagation.
Sleeping 2s...
Warming up WRITE with 75000 iterations...
Failed to connect over JMX; not collecting these stats
WARN  16:06:03,101 Query 'com.datastax.driver.core.Statement$1@4bb5765a;' generated server side warning(s): `USE <keyspace>` with prepared statements is considered to be an anti-pattern due to ambiguity in non-qualified table names. Please consider removing instances of `Session#setKeyspace(<keyspace>)`, `Session#execute("USE <keyspace>")` and `cluster.newSession(<keyspace>)` from your code, and always use fully qualified table names (e.g. <keyspace>.<table>). Keyspace used: keyspace1, statement keyspace: keyspace1, statement id: e1d2f4aa887d02751110f92a52de4f20
Running WRITE with 200 threads for 100000 iteration
Failed to connect over JMX; not collecting these stats
type                                               total ops,    op/s,    pk/s,   row/s,    mean,     med,     .95,     .99,    .999,     max,   time,   stderr, errors,  gc: #,  max ms,  sum ms,  sdv ms,      mb
total,                                                     8,       8,       8,       8,    20.8,    20.1,    25.1,    25.1,    25.1,    25.1,    1.0,  0.00000,      0,      0,       0,       0,       0,       0
total,                                                  1664,    1656,    1656,    1656,    98.7,    84.9,   247.7,   335.5,   467.7,   467.9,    2.0,  0.70339,      0,      0,       0,       0,       0,       0
total,                                                  2700,    1036,    1036,    1036,   184.6,   139.7,   500.4,   584.1,   649.6,   667.4,    3.0,  0.40664,      0,      0,       0,       0,       0,       0
total,                                                  3818,    1118,    1118,    1118,   183.6,   128.7,   574.6,   701.0,   845.7,   850.4,    4.0,  0.38775,      0,      0,       0,       0,       0,       0
total,                                                  5052,    1234,    1234,    1234,   162.6,   103.9,   493.1,   854.1,   987.8,  1058.0,    5.0, -3.00449,      0,      0,       0,       0,       0,       0
total,                                                  6330,    1278,    1278,    1278,   147.3,   112.5,   377.2,   484.7,   573.6,   575.7,    6.0, -5.07481,      0,      0,       0,       0,       0,       0
total,                                                  7317,     987,     987,     987,   179.8,   132.1,   478.4,   663.7,   924.8,   924.8,    7.0,  3.08004,      0,      0,       0,       0,       0,       0
total,                                                  8301,     984,     984,     984,   235.9,   123.9,   618.7,   807.4,  1028.1,  1028.1,    8.0, -1.62741,      0,      0,       0,       0,       0,       0
total,                                                 10052,    1751,    1751,    1751,   112.6,    82.8,   308.0,   530.3,   829.9,   842.0,    9.0, -2.94131,      0,      0,       0,       0,       0,       0
total,                                                 11846,    1794,    1794,    1794,   116.2,    95.9,   291.5,   432.5,   575.7,   599.3,   10.0, -4.19099,      0,      0,       0,       0,       0,       0
total,                                                 13137,    1291,    1291,    1291,   155.9,   113.6,   420.5,   568.3,   683.7,   705.7,   11.0, -7.08575,      0,      0,       0,       0,       0,       0
total,                                                 14809,    1672,    1672,    1672,   106.1,    71.2,   360.4,   549.5,   571.5,   572.5,   12.0,-18.06553,      0,      0,       0,       0,       0,       0
total,                                                 16179,    1370,    1370,    1370,   151.1,   110.0,   364.6,   726.1,   971.0,  1056.4,   13.0, -1.91760,      0,      0,       0,       0,       0,       0
total,                                                 17515,    1336,    1336,    1336,   153.3,   103.0,   472.1,   802.2,   896.5,   986.2,   14.0,  1.54779,      0,      0,       0,       0,       0,       0
total,                                                 18816,    1301,    1301,    1301,   151.1,   104.1,   416.5,   680.0,   858.8,   908.1,   15.0,  1.29148,      0,      0,       0,       0,       0,       0
total,                                                 20232,    1416,    1416,    1416,   140.3,    98.6,   398.5,   596.1,   690.5,   692.1,   16.0,  1.22454,      0,      0,       0,       0,       0,       0
total,                                                 22060,    1828,    1828,    1828,   105.9,    52.3,   363.3,   745.0,   926.9,  1034.9,   17.0,  3.36326,      0,      0,       0,       0,       0,       0
total,                                                 23543,    1483,    1483,    1483,   114.4,    79.9,   353.9,   414.2,   524.3,   572.5,   18.0,  3.07029,      0,      0,       0,       0,       0,       0
total,                                                 23700,     157,     157,     157,   518.3,   156.5,  1303.4,  1339.0,  1344.3,  1344.3,   19.0,  3.10658,      0,      0,       0,       0,       0,       0
total,                                                 24905,    1205,    1205,    1205,   298.1,   135.1,  1443.9,  1707.1,  2035.3,  2185.2,   20.0,  3.18995,      0,      0,       0,       0,       0,       0
total,                                                 27010,    2105,    2105,    2105,    95.4,    73.9,   233.8,   314.6,   559.9,   761.3,   21.0,  2.59731,      0,      0,       0,       0,       0,       0
total,                                                 28301,    1291,    1291,    1291,   136.6,   107.3,   338.4,   476.1,   631.2,   637.5,   22.0,  2.41501,      0,      0,       0,       0,       0,       0
total,                                                 30685,    2384,    2384,    2384,    90.9,    48.1,   334.5,   668.5,   748.7,   806.4,   23.0,  1.94943,      0,      0,       0,       0,       0,       0
total,                                                 32104,    1419,    1419,    1419,   141.2,    94.3,   495.2,   692.1,   855.1,   856.2,   24.0,  1.68828,      0,      0,       0,       0,       0,       0
total,                                                 33762,    1658,    1658,    1658,   115.1,    91.0,   297.3,   405.3,   441.5,   457.7,   25.0,  1.62032,      0,      0,       0,       0,       0,       0
total,                                                 35360,    1598,    1598,    1598,   127.1,    63.7,   427.6,   708.8,   850.4,   855.6,   26.0,  1.41708,      0,      0,       0,       0,       0,       0
total,                                                 37488,    2128,    2128,    2128,    92.9,    50.0,   319.3,   448.5,   532.7,   626.0,   27.0,  1.33034,      0,      0,       0,       0,       0,       0
total,                                                 38843,    1355,    1355,    1355,   128.2,    86.5,   360.2,   526.9,   793.8,   794.8,   28.0,  1.24226,      0,      0,       0,       0,       0,       0
total,                                                 40232,    1389,    1389,    1389,   159.7,    89.7,   451.1,  1288.7,  1398.8,  1451.2,   29.0,  1.28378,      0,      0,       0,       0,       0,       0
total,                                                 41455,    1223,    1223,    1223,   156.8,    94.0,   483.1,   664.3,   926.9,   961.0,   30.0,  0.99197,      0,      0,       0,       0,       0,       0
total,                                                 43299,    1844,    1844,    1844,   115.6,    88.3,   318.2,   415.2,   530.1,   590.3,   31.0,  0.95817,      0,      0,       0,       0,       0,       0
total,                                                 45241,    1942,    1942,    1942,   100.9,    81.0,   252.7,   373.6,   496.2,   498.3,   32.0,  0.93090,      0,      0,       0,       0,       0,       0
total,                                                 46307,    1066,    1066,    1066,   156.4,   131.2,   427.6,   543.7,   610.8,   625.0,   33.0,  0.91189,      0,      0,       0,       0,       0,       0
total,                                                 47248,     941,     941,     941,   218.4,   120.0,   764.9,  1165.0,  1322.3,  1322.3,   34.0,  0.93292,      0,      0,       0,       0,       0,       0
total,                                                 48656,    1408,    1408,    1408,   153.5,    98.4,   543.2,   680.5,   719.8,   724.0,   35.0,  0.89919,      0,      0,       0,       0,       0,       0
total,                                                 50108,    1452,    1452,    1452,   131.7,    42.3,   497.5,   718.3,   910.2,   986.7,   36.0,  0.65465,      0,      0,       0,       0,       0,       0
total,                                                 52296,    2188,    2188,    2188,    97.9,    53.7,   316.1,   535.6,   889.2,  1251.0,   37.0,  0.68129,      0,      0,       0,       0,       0,       0
total,                                                 55172,    2876,    2876,    2876,    71.6,    46.1,   242.2,   331.9,   406.6,   421.3,   38.0,  0.66758,      0,      0,       0,       0,       0,       0
total,                                                 56686,    1514,    1514,    1514,   119.1,    66.2,   380.9,   750.8,   814.7,   820.0,   39.0,  0.64560,      0,      0,       0,       0,       0,       0
total,                                                 58819,    2133,    2133,    2133,    98.6,    60.8,   308.0,   483.1,   583.0,   691.0,   40.0,  0.62858,      0,      0,       0,       0,       0,       0
total,                                                 60917,    2098,    2098,    2098,    95.9,    65.5,   292.8,   392.2,   465.6,   647.5,   41.0,  0.61461,      0,      0,       0,       0,       0,       0
total,                                                 62501,    1584,    1584,    1584,   119.3,    91.9,   303.0,   483.7,   597.2,   602.4,   42.0,  0.60567,      0,      0,       0,       0,       0,       0
total,                                                 63736,    1235,    1235,    1235,   149.6,    91.9,   458.2,   613.9,   761.3,   767.0,   43.0,  0.59410,      0,      0,       0,       0,       0,       0
total,                                                 64917,    1181,    1181,    1181,   169.6,    99.2,   549.5,   817.9,   968.9,   988.8,   44.0,  0.50065,      0,      0,       0,       0,       0,       0
total,                                                 66439,    1522,    1522,    1522,   123.5,    75.6,   411.8,   733.0,  1183.8,  1486.9,   45.0,  0.50571,      0,      0,       0,       0,       0,       0
total,                                                 67146,     707,     707,     707,   239.8,    59.0,   823.7,  1127.2,  1514.1,  1514.1,   46.0,  0.50820,      0,      0,       0,       0,       0,       0
total,                                                 69194,    2048,    2048,    2048,   122.5,    73.9,   308.3,  1173.4,  1459.6,  2025.8,   47.0,  0.51160,      0,      0,       0,       0,       0,       0
total,                                                 70849,    1655,    1655,    1655,   116.8,    83.6,   336.1,   435.4,  2384.5,  2577.4,   48.0,  0.51359,      0,      0,       0,       0,       0,       0
total,                                                 72913,    2064,    2064,    2064,   105.9,    74.0,   262.0,   518.5,  2726.3,  3028.3,   49.0,  0.51552,      0,      0,       0,       0,       0,       0
total,                                                 75364,    2451,    2451,    2451,    80.7,    54.8,   234.5,   327.2,   375.7,   388.0,   50.0,  0.51014,      0,      0,       0,       0,       0,       0
total,                                                 77815,    2451,    2451,    2451,    79.4,    57.9,   221.1,   359.9,   454.0,   626.0,   51.0,  0.50146,      0,      0,       0,       0,       0,       0
total,                                                 80313,    2498,    2498,    2498,    82.4,    47.2,   260.8,   394.8,   507.8,   548.9,   52.0,  0.49436,      0,      0,       0,       0,       0,       0
total,                                                 82465,    2152,    2152,    2152,    90.0,    81.9,   203.4,   288.6,   325.1,   334.8,   53.0,  0.49042,      0,      0,       0,       0,       0,       0
total,                                                 84118,    1653,    1653,    1653,   125.0,    95.2,   337.1,   597.2,   723.0,   731.4,   54.0,  0.48287,      0,      0,       0,       0,       0,       0
total,                                                 86517,    2399,    2399,    2399,    81.3,    48.2,   271.3,   500.2,   566.8,   591.9,   55.0,  0.47588,      0,      0,       0,       0,       0,       0
total,                                                 88512,    1995,    1995,    1995,    89.9,    77.3,   219.5,   348.1,   426.8,   435.4,   56.0,  0.47186,      0,      0,       0,       0,       0,       0
total,                                                 89957,    1445,    1445,    1445,   150.7,    82.8,   540.5,   575.7,   697.3,   848.3,   57.0,  0.46115,      0,      0,       0,       0,       0,       0
total,                                                 91845,    1888,    1888,    1888,   108.5,    65.8,   337.1,   516.7,   592.4,   621.8,   58.0,  0.45575,      0,      0,       0,       0,       0,       0
total,                                                 94286,    2441,    2441,    2441,    81.8,    53.0,   252.2,   342.4,   469.8,   519.0,   59.0,  0.45038,      0,      0,       0,       0,       0,       0
total,                                                 96882,    2596,    2596,    2596,    72.7,    54.8,   215.6,   312.7,   423.4,   464.3,   60.0,  0.44538,      0,      0,       0,       0,       0,       0
total,                                                 98527,    1645,    1645,    1645,    78.2,    39.3,   293.9,   439.6,   515.6,   522.2,   61.0,  0.44195,      0,      0,       0,       0,       0,       0
total,                                                100000,    1931,    1931,    1931,   147.0,    78.5,   575.1,   696.8,   760.7,   980.9,   61.8,  0.45003,      0,      0,       0,       0,       0,       0


Results:
Op rate                   :    1,619 op/s  [WRITE: 1,619 op/s]
Partition rate            :    1,619 pk/s  [WRITE: 1,619 pk/s]
Row rate                  :    1,619 row/s [WRITE: 1,619 row/s]
Latency mean              :  120.5 ms [WRITE: 120.5 ms]
Latency median            :   76.1 ms [WRITE: 76.1 ms]
Latency 95th percentile   :  376.4 ms [WRITE: 376.4 ms]
Latency 99th percentile   :  652.7 ms [WRITE: 652.7 ms]
Latency 99.9th percentile : 1397.8 ms [WRITE: 1,397.8 ms]
Latency max               : 3028.3 ms [WRITE: 3,028.3 ms]
Total partitions          :    100,000 [WRITE: 100,000]
Total errors              :          0 [WRITE: 0]
Total GC count            : 0
Total GC memory           : 0.000 KiB
Total GC time             :    0.0 seconds
Avg GC time               :    NaN ms
StdDev GC time            :    0.0 ms
Total operation time      : 00:01:01

END
```

# Результаты нагрузочного тестирования Cassandra

## Основные метрики производительности

### Общая производительность:
- **Скорость операций**: `1,619 операций/сек` (только запись)  
- **Всего записей**: `100,000 партиций` за `61.8 секунд`  

### Задержки (latency):
| Метрика               | Значение   |
|-----------------------|------------|
| Средняя задержка      | 120.5 мс   |
| Медианная задержка    | 76.1 мс    |
| 95-й перцентиль       | 376.4 мс   |
| 99-й перцентиль       | 652.7 мс   |
| Максимальная задержка | 3028.3 мс  |

## Динамика выполнения теста

### Начальная фаза (0-10 сек)
- Кластер в режиме прогрева
- Колебания производительности
- Пиковые задержки: `до 850 мс`

### Стабильная фаза (10-50 сек)
- Стабильная производительность: `~2000 оп/сек`
- Средние задержки: `70-100 мс`
- Оптимальный режим работы

### Финальная фаза (50-61.8 сек)
- Сохранение стабильности
- Единичные выбросы задержек: `до 3028 мс`
- Возможные причины: GC паузы или сетевые задержки

> **Вывод**: Кластер демонстрирует стабильную производительность при нагрузке ~2000 записей/сек с задержками <500мс в 95% случаев.

