### Create VPC stack
> aws cloudformation create-stack --stack-name esdc --template-body file://vpc.json 


### Create VPC stack
> aws cloudformation create-stack --stack-name esdc --template-body file://vpc.json --parameters  ParameterKey=Parm1,ParameterValue=test1 

### Delete VPC satck
> aws cloudformation delete-stack --stack-name esdc-vpc