paragraph = """Russia's overnight attack on the southern Ukrainian port city of Odesa was a "pathetic attempt at retaliation" the Ukraine Defense Ministry said Monday on social media.

The ministry contended that the Kremlin was responding to Ukrainian attack on Russia's Black Sea Fleet headquarters in Sevastopol on Friday.

Ukraine's military alleged that Russia's attack on Odesa was a violation of international humanitarian law, as it targeted both troops and civilian infrastructure, including the power supply."""

#Converting the whole paragraph into lowercase
paragraph.lower()
paragraph1 = paragraph.lower()
print(paragraph)
print(paragraph1)


#Counting the number of whitespaces in the paragraph
paragraph.count(" ")
print(paragraph.count(" "))

#Finding the count of "the", "that" and "for" in the paragraph
the_count = paragraph.count("the")
that_count = paragraph.count("that")
for_count = paragraph.count("for")
print(the_count)
print(that_count)
print(for_count)


#total length of the paragraph
len(paragraph)
print(len(paragraph))

#replace "the", "that" and "for" with "YAY"
rep_the = paragraph.replace("the", "YAY")
rep_that = paragraph.replace("that", "YAY")
rep_for = paragraph.replace("for", "YAY")

paragraph2 = rep_the
paragraph3 = rep_that
paragraph4 = rep_for

print(paragraph2)
print(paragraph3)
print(paragraph4)

