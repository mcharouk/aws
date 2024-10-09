# Relation Embedding, Self Attention, Feed Forward

Let's imagine you're building an LLM to translate English to French. You input the sentence:

> The cat sat on the mat

 Here's how the components work together:

## Embedding:

* Each word in the sentence ("The", "cat", "sat", etc.) is first transformed from a simple string of characters into a vector, a list of numbers representing its meaning and relationship to other words. This is the "embedding" of the word.
* For example, the embedding for "cat" might encode that it's a furry, domesticated animal often kept as a pet.

## Self-Attention:

* Now, imagine the model needs to figure out what "it" refers to in the sentence

> The cat sat on the mat. It was very soft 

* Self-attention helps the model understand the relationships between words, even across longer distances. It would recognize that "it" likely refers to the "mat" because of their proximity and the context of sitting on something soft.

## Feed-Forward Network:

* With the contextual information provided by self-attention, the feed-forward network now processes each word's embedding to generate the French translation.
* For "cat," the network might initially consider translations like "chat" (male cat) or "chatte" (female cat).
* However, because self-attention highlighted the relationship between "cat" and "it" (referring to the soft mat), the feed-forward network can deduce that the gender of the cat is irrelevant in this context and simply use "chat," the general word for "cat"

## In summary:

* Embedding: Provides the initial meaning of individual words.
* Self-attention: Analyzes relationships between words to provide context.
* Feed-forward network: Uses the word embeddings and contextual information to perform the translation, taking into account the relationships highlighted by self-attention.


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

> From now on, I would like you to ask me questions to [do a specific task]. When you have enough information to [do the task], create [output you want].

## Question Refinement Pattern


> From now on, when I ask a question, suggest a better version of the question to use that incorporates information specific to [use case] and ask me if I would like to use your question instead.

## The Cognitive Verifier Pattern

> When I ask you a question, generate three additional questions that would help you give a more accurate answer. When I have answered the three questions, combine the answers to produce the final answers to my original question.


# Few Shot Prompt

[Langchain Example selector](https://python.langchain.com/v0.1/docs/modules/model_io/prompts/example_selectors/)

## Sentence 1

Phrase originale

> Research firm fends off allegations of impropriety over new technology.


Traduction


> Un cabinet de recherche réfute les allégations d'irrégularités concernant une nouvelle technologie.


## Sentence 2


Phrase originale

> Offshore windfarms continue to thrive as vocal minority in opposition dwindles.


Traduction

> Les parcs éoliens offshore continuent de prospérer alors que la minorité qui s’y oppose s’amenuise.



## Sentence 3

Phrase originale

> Manufacturing plant is the latest target in investigation by state officials.


Traduction

> L'usine de fabrication est la dernière cible d'une enquête menée par les autorités de l'État.


## Insights

* Inverting True or False has no effect on the final result. The effect is mainly on output format.
Some LLM (Claude ?) has even told me that my feeling were probably inverted before giving me its final answer

* Interesting insight : when i add some context, for instance 

> You are an environmental activist who fights against companies that commit harmful acts against the environment

the LLM changes its output to match the role, it no more stands with the company.