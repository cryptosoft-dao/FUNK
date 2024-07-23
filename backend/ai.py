import requests

print(requests.post("https://api.telegram.org/bot7194502673:AAEk2mq9vkmZncd7luD1t7tSh1UoEJEPHhU/deleteWebhook",json={'url':'https://automation.production.tookey.cloud/api/v1/webhooks/vhNPBikkulvFGoj11vEyn'}).json())