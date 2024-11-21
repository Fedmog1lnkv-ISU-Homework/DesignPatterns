curl -X PATCH ^
  "http://127.0.0.1:8000/api/api/nomenclature/e891b718-9051-4b02-81bd-ec8f01cc44f0" ^
  -H "accept: application/json" ^
  -H "Content-Type: application/json" ^
  -d "{\"name\": \"new_name\"}"
