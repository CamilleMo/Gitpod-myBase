curl -X POST -H "Content-Type:application/json; format=pandas-­split" –data "CONTENT_OF_INPUT_JSON"  "http://127.0.0.1:1235/invocations"
curl -X POST -H "Content-Type:application/json" –data "{1,2,3}"  "http://127.0.0.1:1235/invocations"