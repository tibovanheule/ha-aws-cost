import boto3
import asyncio
import concurrent.futures
from datetime import date, datetime, timedelta
import logging
import calendar

_LOGGER = logging.getLogger(__name__)

class AWSCostExplorer:
    def __init__(self, aws_access_key_id, aws_secret_access_key, region_name):
        _LOGGER.debug("Initializing AWSCostClient with AWS access key: %s and region: %s", aws_access_key_id, region_name)
        
        self.client = boto3.client('ce',
                                    aws_access_key_id=aws_access_key_id,
                                    aws_secret_access_key=aws_secret_access_key,
                                    region_name=region_name)

    def get_month_to_date_cost(self):
        _LOGGER.debug("Preparing to fetch cost data using boto3 client.")
        try:
            start = str(date.today().replace(day=1))    
            end = str(date.today() + timedelta(days=1))

            response = self.client.get_cost_and_usage(
                TimePeriod = {
                    'Start': start,
                    'End': end
                },
                Granularity="MONTHLY",
                Metrics=[
                    "BlendedCost"
                ]
            )

            _LOGGER.debug("Received response from AWS Cost Explorer: %s", response)

            amount = response['ResultsByTime'][0]['Total']['BlendedCost']['Amount']
            currency = response['ResultsByTime'][0]['Total']['BlendedCost']['Unit']

            _LOGGER.debug("Costs: %s %s", amount, currency) 

            return amount, currency

        except Exception as e:
            _LOGGER.error("Error occurred while fetchung cost data: %s", e)



    def get_cost_forecast(self):
        _LOGGER.debug("Preparing to fetch cost data using boto3 client.")

        try: 
            if date.today().day == calendar.monthrange(date.today().year, date.today().month)[1]: 
                start = str(date.today().replace(day=-1))
                _LOGGER.debug("Start: %s", start)
            else:
                start = str(date.today())

            end = str(date.today().replace(day=calendar.monthrange(date.today().year, date.today().month)[1]))  
            
            response = self.client.get_cost_forecast(
                TimePeriod = {
                    'Start': start,
                    'End': end
                },
                Granularity="MONTHLY",
                Metric="BLENDED_COST"
            )
            
            _LOGGER.debug("Received response from AWS Cost Explorer Forecast: %s", response)   
            amount = response['Total']['Amount']
            currency = response['Total']['Unit']    
            _LOGGER.debug("Costs: %s %s", amount, currency) 
            
            return amount, currency
        except Exception as e:
            _LOGGER.error("Error occurred while fetchung cost data: %s", e)