# Python Object Relational Mapping

## MySQLdb Scripts
```bash
./0-select_states.py root root db_name
./1-filter_states.py root root db_name
./2-my_filter_states.py root root db_name 'Arizona'
./3-my_safe_filter_states.py root root db_name 'Arizona'  # SQL injection safe
./4-cities_by_state.py root root db_name
./5-filter_cities.py root root db_name 'Texas'
```

## SQLAlchemy ORM
```bash
./7-model_state_fetch_all.py root root db_name
./8-model_state_fetch_first.py root root db_name
./9-model_state_filter_a.py root root db_name
./10-model_state_my_get.py root root db_name 'Texas'
./11-model_state_insert.py root root db_name
./12-model_state_update_id_2.py root root db_name
./13-model_state_delete_a.py root root db_name
./14-model_city_fetch_by_state.py root root db_name
```

**Models:** `model_state.py`, `model_city.py`