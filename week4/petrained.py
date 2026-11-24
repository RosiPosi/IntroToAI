import gensim.downloader as api

model = api.load("glove-wiki-gigaword-50")   # ~66MB, downloads once
print(model.most_similar("glass"))

# [('plastic', 0.79425048828125), ('metal', 0.7708716988563538), ('walls', 0.7700635194778442), 
# ('marble', 0.7638523578643799), ('wood', 0.7624280452728271), ('ceramic', 0.7602593302726746), 
# ('pieces', 0.7589112520217896), ('stained', 0.7528817653656006), ('tile', 0.748193621635437), ('furniture', 0.7463858723640442)]

#TOP 5 WORDS SIMILAR TO GLASS:
#[('plastic', 0.79425048828125), ('metal', 0.7708716988563538), ('walls', 0.7700635194778442), ('marble', 0.7638523578643799), ('wood', 0.7624280452728271)]

#Words similar to bank:
#[('banks', 0.869862973690033), ('securities', 0.7996813654899597), ('banking', 0.7965160012245178), ('investment', 0.7849708199501038), ('exchange', 0.7808825969696045)]

#Words similar to bat:
#[('bats', 0.7963688969612122), ('wicket', 0.7592863440513611), ('catch', 0.7541334629058838), ('balls', 0.7539033889770508), ('ball', 0.7205045223236084)]

#Words similar to algorithm:
#[('algorithms', 0.8708400130271912), ('iterative', 0.8088648915290833), ('optimization', 0.7956129312515259), ('compute', 0.7942942976951599), ('computation', 0.791283369064331)]

#Words similar to photosynthesis:
#[('respiration', 0.7888653874397278), ('photosynthetic', 0.7678346633911133), ('oxygenic', 0.7276953458786011), ('uptake', 0.7008628249168396), ('algae', 0.6988705396652222)]

#AMBIGUOUS WORD: BANK
#[('banks', 0.869862973690033), ('securities', 0.7996813654899597), ('banking', 0.7965160012245178), ('investment', 0.7849708199501038), ('exchange', 0.7808825969696045), ('financial', 0.7670274972915649), ('credit', 0.764915406703949), ('lender', 0.7518407702445984), ('capital', 0.7380707859992981), ('brokerage', 0.7373986840248108)]

# AMBIGUOUS WORD: BAT
# [('bats', 0.7963688969612122), ('wicket', 0.7592863440513611), ('catch', 0.7541334629058838), ('balls', 0.7539033889770508), ('ball', 0.7205045223236084), ('pitch', 0.7166818380355835), ('opener', 0.7043341398239136), ('bowled', 0.6956043243408203), ('batsman', 0.694519579410553), ('tendulkar', 0.6740003228187561)]

#WORD PAIR SIMILARITIES:
#cat - dog: 0.9218
#car - bicycle: 0.7560
#cat - democracy: 0.0368

# The word "bank" has multiple meanings, including a financial institution and the side of a river.
# GloVe model may return words associated with both meanings because it was trained on raw text 
# without being told which meaning is intended. It learns word relationships by looking at the contexts in which words appear.
# Results mainly showed words related to finance, such as "securities", "investment", "credit" and "lender". This suggests that the model mostly associates the word "bank" with its financial meaning.
# Same with bats. I would imagine the animal, but GloVe thought of the sport.

# There are some words I would've expected to have higher accuracy, like photosynthesis and photosynthetic or bank and banking.
# I chose three word pairs with different expected levels of similarity. Cat and dog had a high similarity score of 0.9218, 
# which makes sense because they are both animals and often appear in similar contexts. Car and bicycle had a similarity score of 0.7560, 
# which was also relatively high because both are forms of transportation. 
# Cat and democracy had a much lower score of 0.0368, as they have very different meanings and are generally used in different contexts. 
# Overall, the results matched my expectations.