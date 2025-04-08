# Bedrock Demo

* Better to make the demo in us-east-1 because image generation is currently not available in eu-west-3 region
  
## Text 

* [Original blog post](https://www.aboutamazon.com/news/aws/generative-ai-is-the-future)
* Go on Bedrock -> Chat/Text
* Select Mode : Single Prompt
* Select Nova Lite model
* copy this text

```
Summarize this text for me in a few bullet points. 
Add a specific paragraph that lists all the possible use cases that Generative AI makes possible

Text : Think back to when a new set of technologies or a tech-enabled gizmo completely grabbed your attention and imagination. The first personal computers. The advent of the internet and the web. Email. Smartphones. These things changed our lives in ways that were hard to anticipate, and to perhaps appreciate, until we had some time with these technologies under our collective belts.

We are at that moment again with artificial intelligence (AI) and machine learning (ML). I believe AI and ML are the most transformational technologies of our time. Which is why, for more than 20 years, Amazon has invested heavily in the development of AI and ML, infusing these amazing capabilities into nearly every business unit.

Why generative AI is in the spotlight
AI used to be the domain of a small group of researchers and data scientists. Today, you can’t open a newsfeed without some reference to AI and specifically generative AI. It may come as a surprise, but the concepts of AI have been around since the 1950s.
So why is this technology—which has been percolating for decades—seeing so much interest now? Simply put, AI has reached a tipping point thanks to the convergence of technological progress and an increased understanding of what it can accomplish. Couple that with the massive proliferation of data, the availability of highly scalable compute capacity, and the advancement of ML technologies over time, and the focus on generative AI is finally taking shape.

Plus, it’s highly likely that you already have experience using AI and ML. If you have listened to a Wondery podcast, asked Alexa for today’s forecast, searched Prime Video for a new series, or visited a store with Just Walk Out technology, you tapped into AI from Amazon. More specifically, you interacted with ML systems or models. It is these ML models that sit at the center of the generative AI excitement and potential.
So, what exactly is generative AI? And how is it different from other AI?
Although based on the same concepts, there is a straightforward distinction between AI’s traditional machine learning techniques that we’ve been putting to work for years—in particular deep learning—and generative AI. As its name suggests, generative AI is a type of artificial intelligence that can create new content and ideas. It can be text, images, video, voice, and even code. Like all AI, generative AI is powered by machine learning models—very large ML models that are pre-trained on vast amounts of data and commonly referred to as foundation models (FMs).

Before we put FMs to work, traditional forms of machine learning allowed us to take simple inputs, like numeric values, and map them to simple outputs, like predicted values. With more advanced ML techniques, especially deep learning, we could take somewhat more complicated inputs, like videos or images, and map them to relatively simple outputs. You could look for an image in a video stream that ran afoul of guidelines, or analyze a document for sentiment. With this approach, you get insight into the data that you give the model, but you don’t generate anything new. With generative AI, you can leverage massive amounts of data—mapping complicated inputs to complicated outputs—and create new content of all kinds in the process.
Traditional ML models also tend to be task-specific. If I wanted to do translation with a deep learning model, for example, I would access lots of specific data related to translation services to learn how to translate from Spanish to German. The model would only do the translation work, but it couldn’t, for example, go on to generate recipes for paella in German. It could translate a paella recipe from Spanish into German that already exists, but not create a new one.

Now, with generative AI, everyone can use AI without the manual data prep. The large models that power generative AI applications—those foundation models—are built using a neural network architecture called “Transformer.” It arrived in AI circles around 2017, and it cuts down development process significantly.
Using Transformer architecture, generative AI models can be pre-trained on massive amounts of unlabeled data of all kinds—text, images, audio, etc. There is no manual data preparation, and because of the massive amount of pre-training (basically learning), the models can be used out-of-the-box for a wide variety of generalized tasks. It’s a bit like the Swiss Army knife of AI.

A model can learn in the pre-training phase, for example, what a sunset is, what a beach looks like, and what the particular characteristics of a unicorn are. With a model designed to take text and generate an image, not only can I ask for images of sunsets, beaches, and unicorns, but I can have the model generate an image of a unicorn on the beach at sunset. And with relatively small amounts of labeled data (we call it “fine-tuning”), you can adapt the same foundation model for particular domains or industries.
Generative AI applications: Generative AI will transform how every company and organization operates
The ability to customize a pre-trained FM for any task with just a small amount of labeled data─that’s what is so revolutionary about generative AI. It’s also why I believe the biggest opportunity ahead of generative AI isn’t with consumers, but in transforming every aspect of how companies and organizations operate and how they deliver for their customers.
In health care, the legal world, the mortgage underwriting business, content creation, customer service, and more, we anticipate expertly tuned generative AI models will have a role to play. Imagine if automated document processing made filing your taxes simple and fast, and your mortgage application a straightforward process that lasted days, not weeks. What if conversations with a health care provider were not only transcribed and annotated in plain speak, but offered the physician potential treatments and the latest research? Or what if you could explore the design of a new product, optimizing for sustainability, cost, and price with simple prompts. All of these are not just possible but likely with generative AI.

Already we are seeing a pattern emerge in how generative AI will show up in businesses across four main modalities.
Improving the customer experience through capabilities such as chatbots, virtual assistants, intelligent contact centers, personalization, and content moderation.
Boosting employees’ productivity with conversational search, text summarization, and code generation, among others.
Producing all types of creative content from art and music to text, images, animations, and video.
Improving business operations with intelligent document processing, maintenance assistants, quality control and visual inspection, and synthetic training data generation.

The key is to ensure that you actually pick the right AI-enabled tools and couple them with the right level of human judgment and expertise. These models are not going to replace humans; they are just going to make us all vastly more productive. More importantly, you need to tune these models with your data in a secure manner, so, at the end of the day these models are customized for the needs of your organization. Your data is the differentiator and key ingredient in creating remarkable products, customer experiences, or improved business operations.
Like the internet in 1995
These are still very early days for generative AI. There is so much more to be invented and iterated upon. It reminds me of the internet circa 1995, when the web was just beginning to happen, and we heard about this thing called a web browser.

When you step back and look at where we are today, and what is yet to come, generative AI has the potential to revolutionize our lives, whether at home, school, or work. With these tools Amazon and our customers are building, we’ll all be able to spend more time on what we are best at, and less time on the routine work. That is quite powerful, and that's what is going to make this such an incredible time.
```

## Image

* For image, go to **us-east-1** region
* Go to Bedrock -> Image/Video
* select **Nova Canvas**

```
a cat enjoying a mojito in front of an Italian-style villa on the edge of a lake
```