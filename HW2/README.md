# ДЗ-2
## Здание 1: Установить и настроить Prometheus, замониторить пром.

Для установки были проделаны все шаги из инструкции к семинару. Установка по данной инструкции также включает мониторинг самого Prometheus.
На машине запущен сервис Prometheus, для подключения к UI:
```bash
ssh -L 9090:127.0.0.1:9000 ubuntu@130.193.50.69
```
На `localhost:9090` появится UI Prometheus.
![Prometheus_UI](Prometheus_UI.png)

## Задание 2: Показать использование PromQL

Создадим несколько тестовых запросов:
1. Сумма длительностей http-запросов с момента последнего рестарта
```bash
prometheus_http_request_duration_seconds_sum
```
![query_easy](pics/query_easy.pnd)
2. Длительность http-запросов за последние 10 минут для эндпоинта "/metrics"
```bash
rate(prometheus_http_request_duration_seconds_sum{handler="/metrics"}[10m])
```
![query_medium](pics/query_medium.pnd)
3. Средня длительность http-запросов за 10 минут для эндпоинта "/metrics" за последний день c шагов в 10 минут
```bash
avg_over_time(rate(prometheus_http_request_duration_seconds_sum{handler="/metrics"}[10m])[1d:10m])
```
![query_hard](pics/query_hard.pnd)


## Задание 3: Записать recording rule для какого-либо сложного вычисления.

Создадим recording rule для последнего запроса. Для этого:
1. Добавим файл `rules.yml` в `/etc/prometheus`
2. Пропишем путь до него в `prometheus.yaml`
Перезапускаем сервис и проверяем что правило существует:
![query_rule](pics/query_rules.pnd)