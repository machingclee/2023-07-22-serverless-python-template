- (for conda) To include new dependency, we simply 
  ```
  pip install <the_dependecy_name> && pip freeze > requirements.txt
  ```
- `sls wsgi serve` to start locally
- `sls plugin install -n serverless-wsgi`
- `sls plugin install -n serverless-python-requirements`
