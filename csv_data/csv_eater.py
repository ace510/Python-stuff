import csv, string
from collections import Counter

csv_file = open("foia_150k_plus.csv")
reader = csv.reader(csv_file)
table = str.maketrans(dict.fromkeys(string.punctuation))

# no_punctuation= punctuation_to_remove.translate(table)

schema = next(reader)
# ['LoanRange', 'BusinessName', 'Address', 'City', 'State', 'Zip', 'NAICSCode',
#  'BusinessType', 'RaceEthnicity', 'Gender', 'Veteran', 'NonProfit',
# 'JobsRetained', 'DateApproved', 'Lender', 'CD']

for company in reader:
    if "sage" in company[1].lower().split(" ") and "software" in company[
        1
    ].lower().split(
        " "
    ):  # and company[4] == 'OR'
        print(company)


# common_terms = Counter()

# comp = next(reader)

# print(comp[1])
# print(comp[1].split(' ') )
# lister = comp[1].split(' ')
# for i in lister:
#     print(i)

# for i in reader:
#     for word in i[1].split(' '):
#         word_fixed = word.strip()
#         common_terms[word] += 1

# print(common_terms.most_common(50))

# a golfball is 1.68 inches
