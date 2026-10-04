import dlt

@dlt.table
def transformed_data():
  return spark.range(10)