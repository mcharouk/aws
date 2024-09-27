# References

* [Advanced Prompting techniques](https://aws.amazon.com/blogs/machine-learning/implementing-advanced-prompt-engineering-with-amazon-bedrock/)
* [self-consistency prompting](https://aws.amazon.com/blogs/machine-learning/enhance-performance-of-generative-language-models-with-self-consistency-prompting-on-amazon-bedrock/)

# COSTAR

* Context : Providing background information helps the FM understand the specific scenario and provide relevant responses
* Objective : Clearly defining the task directs the FM’s focus to meet that specific goal
* Style : Specifying the desired writing style, such as emulating a famous personality or professional expert, guides the FM to align its response with your needs
* Tone : Tone of the response : humorous, poetic, entertaining, formal.
* Audience : What audience the response is targeting. For example if the audience are beginners or technical experts.
* Response : output format


# Interesting reflection patterns

[Reference](https://www.descript.com/blog/article/5-advanced-prompts-to-get-better-answers-from-chatgpt)

## Flipped Interaction PAttern

```
From now on, I would like you to ask me questions to [do a specific task]. When you have enough information to [do the task], create [output you want].
```

* this method 

## Question Refinement Pattern

```
From now on, when I ask a question, suggest a better version of the question to use that incorporates information specific to [use case] and ask me if I would like to use your question instead.
```

## The Cognitive Verifier Pattern

```
When I ask you a question, generate three additional questions that would help you give a more accurate answer. When I have answered the three questions, combine the answers to produce the final answers to my original question.
```
