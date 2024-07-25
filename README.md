# ha-aws-cost - AWS Cost custom component for Home Assistant

The ha-aws-cost custom component interacts with AWS to get the month to date cost and forecast cost and make it available on Home Assistant. It adds two new entities:

* **Month to date cost:** The current cost of your AWS account 
* **Forecasted month costs:** The forecasted cost based in your current consumption 

## Pre-requirements
1. You'll need an 'Access Key ID' and a 'Secret Access Key' to set the integration up. I strongly recommend you to create a new IAM user and policy with the following permissions:

    ```json
    # aws-iam-policy.json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": [
                    "ce:GetCostAndUsage",
                    "ce:GetCostForecast"
                ],
                "Resource": "*"
            }
        ]
    }
    ```

In case you don't know how to generate the credentials, please read the following documentation: [Managing access keys for IAM users
](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey)


## Installation

### Option 1: HACS

First, install the custom integration using [HACS](https://hacs.xyz/).

1. Add the integration using HACS
2. Restart Home Assistant

[![](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=diego7marques&repository=ha-aws-cost)

### Option 2: Manual installation

1. Download and copy the `custom_components/aws_cost` directory into the `custom_components` folder on your home assistant installation.

2. Restart Home Assistant

## Setup

Once installed, go to `Settings > Devices & services > + Add integration > AWS Cost`. The setup will request 4 inputs:

1. **AWS Access Key ID**: _Access key generated for the IAM user._
2. **AWS Secret Access key**: _Access Secret key generated for the IAM User._
3. **AWS Region**: _Your default region. As Cost Explorer is a global resource, the region will only be used to adquire the token._
4. **Update Frequency**: _How many times you want your data to be updated a day. The options are: `Daily`, `Every 12 hours` and `Every 6 hours`._

## Considerations

* AWS charges $0.01 for any request done to AWS Cost Explorer API. For more information: [AWS Cost Explorer Pricing](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/pricing/#:~:text=Cost%20Explorer%20offers%20hourly%20granularity,specific%20resource%20and%20usage%20type.)

    _NOTE: Each pooling to update the entity state makes two requests to AWS CostExplorer API, using the `GetCostandUsage` and `GetCostForecast` operations._

* The costs shown may not always be up-to-date, as AWS explains:

    >"Cost Explorer refreshes your cost data at least once every 24 hours. However, this depends on your upstream data from your billing applications, and some data might be updated later than 24 hours."

    Reference: [Analyzing your costs with AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html)