import dlt

@dlt.table
def trasnsformed():
  return spark.range(10)