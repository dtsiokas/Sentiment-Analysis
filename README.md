# Sentiment-Analysis

# I.	 	Introduction
For this project, I analyzed 3 articles about America’s job market and how way fewer jobs were added in April 2021. Employers looking for workers couldn't find them, while many laid-off people remained on the sidelines waiting for a return to normalcy. For my project, I wanted to see which words have the most impact on the sentiment of an event like this. I used three articles from different news outlets which were Wall Street Journal (WSJ), CNBC and CNN. These articles were first all placed into the Sentiment Analysis tool to get the scores of each. The texts were then saved as .txt files to be cleaned later. Afterwards, using Python I was able to stem the text files, remove all stopwords and tokenize the rest of the elements in the text. This was done for all three of the documents individually. The python script then saves the cleaned text as a .txt file which was then processed through Voyant. After plugging the cleaned data into Voyant we were able to determine which 10 words had the most significance in the articles as well as their frequency. Finally, these words were put into Excel for Term Frequency-Inverse Document Frequency (tf-idf) coding to determine the weight of each of those 10 words.



# II.	The Analysis
I first used the Sentiment Analysis tool to receive the sentiment scores of each article. As a result I determined that the CNN article had the most negative tone of -82.8

![Screenshot (39)](https://user-images.githubusercontent.com/71915516/151673693-34a77ec3-5048-47b4-8b5e-e2c0048fd793.png)


CNBC article is essentially neutral and has a sentiment score of 0.9

![Screenshot (40)](https://user-images.githubusercontent.com/71915516/151673705-1e9cfcb3-96f2-4a70-9cc3-f7bce4d8b051.png)


and WSJ article is somewhat positive with the score of 25.2

![Screenshot (41)](https://user-images.githubusercontent.com/71915516/151673714-51d35499-5770-4d49-94f1-1f139c2789d2.png)


Seeing as these were the results of the sentiment, I then cleaned the data with Python

![Screenshot (149)](https://user-images.githubusercontent.com/71915516/151679991-ec208033-1a96-459c-937f-343d30c838ac.png)



Afterwards I used Voyant Text Analysis to determine which words were the most frequent and which words had the most significance for each article. For the WSJ article the words with the most significance were: workers(11), april(10), jobs(10), labor(9), pandemic(9), rate(8), month(7), people(7), unemployment(7), average(6)

![Screenshot (47)](https://user-images.githubusercontent.com/71915516/151674421-1ff35fd4-18c3-45ec-8054-85da0f7586ba.png)


For the CNBC article the words with the most significance were: jobs(7), rate(6), amid(5), hiring(5), level(5), march(5), pace(5), people(5), workers(5), employment(4)

![Screenshot (46)](https://user-images.githubusercontent.com/71915516/151674463-fb551556-3b1f-40d2-9660-ead9a8905e45.png)


For the CNN article the most significant words were: jobs(1), month(1), pandemic(1), market(7), april(1), labor(1), economists(5), workers(5), employment(4), million(4)

![Screenshot (45)](https://user-images.githubusercontent.com/71915516/151674472-08a90319-b9a0-41b2-8230-b1db104a423c.png)


Using EXCEL, I did binary and frequency coding to visualize these numbers. Afterwards, I performed tf-idf coding in order to see the weight of each word. Using this, I was able to then compare the weight of each word corresponding to each article to determine which word or words had the greatest impact on the sentiment of an article. The WSJ article had the most positive sentiment, and the words with the most significance were “workers”, “unemployment” and “average”. CNBC had a neutral sentiment and the most impactful words were “hiring”, “level”, “march” and “pace”. CNN’s article was the most negative article and its most impactful words were “market”, “economists”, and “million”.


![Screenshot (148)](https://user-images.githubusercontent.com/71915516/151674829-61504bf8-e03b-4f3c-91ea-c760bc16aac0.png)




# III.	Conclusion
In conclusion, the April jobs report fell very short of expectations. Many news outlets reported on the news in their own way with their own agendas. My analysis took in three articles from WSJ, CNBC and CNN, respectively. After having stemmed, removed stopwords and tokenized the .txt files in Python, I then plugged each cleaned file into the Sentiment Analysis tool. Sentiment analysis showed that WSJ had a positive sentiment, CNBC a neutral sentiment and CNN with a very negative sentiment. Using Voyant I was able to determine which words had the most significance and the frequency of those articles. Finally, after having done binary and frequency coding, I constructed a matrix for Term Frequency-Inverse Document Frequency to determine the weight of the most significant words. This helped to determine which words held the most weight in the positive, neutral and negative article. My analysis can help in determining which writers are more negative on certain topics and which are more positive. It can also help, if used on a much larger scale, in determining which words to use if a company wishes to (or does not wish to) write with a more negative, positive or neutral sentiment.

