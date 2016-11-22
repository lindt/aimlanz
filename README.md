# aimlanz - Insurance Chat Bot Mockup

Goal is to reduce service and acquisition costs for insurance companies.
Getting the insurance needs for the customer out of a conversation.

Chat Bot based on AIML - Artifical Intelligence Markup Language

## Advantages

 - based on existing NLTP technology
 - Usage of aiml for insurance specific questions and knowledge acquisition
 - Offers are calculated in Python itself to be able to query existing databases

## Example usage

It loads a special tailored insurance aiml file
`Loading allianz.aiml... done (0.00 seconds)`

Then you can interact with the bot and
`Enter your message >> my dogs name is Mike`

Answer:
`That is interesting that you have a dog named Mike`

Ask for insurances:
`Enter your message >> what personal offers do you have?`

Answer:
`Your personal offers are: A generic dog insurance,but we can tailor it to your need if you tell us your dogs race. If you take them all, you will get 5% discount`

Add more details on the Dog:
`Enter your message >> my dog is a pitbull`

Answer:
`These days many people have pitbull dogs`

Ask again for insurances:
`Enter your message >> what personal offers do you have?`

Answer:
`Your personal offers are: A dog insurance for your pitbull If you take them all, you will get 5% discount`

Add more personal details:
`Enter your message >> i have a car from BMW`

Answer:
`That is interesting that you have a car from BMW`

Ask for insurances and now also get a car insurance offered:
`Enter your message >> what personal offers do you have?`

Answer:
```Your personal offers are: A car insurance
A dog insurance for your pitbull If you take them all, you will get 10% discount```
