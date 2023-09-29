import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

import json


SUBSCRIPTION = 'projects/project-id/subscriptions/subscription'
TABLE = 'project-id.dataset.table_sensor'

pipeline_options = PipelineOptions(
    runner='DataflowRunner',
    project='project-id',
    region='us-central1',
    temp_location='gs://bucket_temporario/temp',
    streaming=True
)


def main():
    with beam.Pipeline(options=pipeline_options) as pipeline:(
        pipeline
        | 'Read' >> beam.io.ReadFromPubSub(subscription=SUBSCRIPTION)
        | 'Decode' >> beam.Map(lambda x: json.loads(x.decode('utf-8')))
        | 'Write BigQuery Table' >> beam.io.WriteToBigQuery(TABLE,
                                    schema='lux:STRING,temperatura:STRING,umidade:STRING,data_sensor:STRING',
                                    write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND)
    )

if __name__ == '__main__':
    main()