# Pre-test for LINE Tech Fresh

## Environment

1. line-bot-sdk for building line bot with python
2. flask for server backend

## Implementation

First questions are read from line bot interface. Once a question successfully matches the predifined cases, the response is then given through webhook.

## Special Feature

To demonstrate my ongoing fake news detection project, I tried making a possible user interface with line bot. When a user says "呼叫阿水伯！", the following message will be processed and classified by a currently weak classifier trained with LSTM and message data from Cofacts. The classifier then throws four kinds of outputs including "not articles", "not rumors", "personal opinions" or "rumors".

However, due to the limited amount of data and deadline for this homework, the classifier got a huge room for improvement. Don't totally trust it!