# Job_Info_Spidler
This is a python script for scratching job info from zhipin.com.

## What it does?
It can get the job info from the [website](https://zhipin.com), write the content to "info.md" and send itself to your mailbox. 

## How it runs?
You just need to fill the secret key of e-mail and the target e-mail in 'run.py';
```python
receivers = ['xxxxx@xxxxxxx.com']   # target e-mail
mail_host = "smtp.xx.com"           # server address
mail_user = "xxxxxxxxxx@xx.com"     # sender's e-mail
mail_pass = "mxxxxxxxxxxxxxxx"      # secret key
sender = 'xxxxxxxxxx@xx.com'        # sender
```
Of course you also need to fill the job description.

```python
template_city = ['101020100', '101190100']  # city_code
template_description = ['BI', 'spidler engineer'] # job descriptions
```

## Other
You need to ensure your IP is available in this site.
