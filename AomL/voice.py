import sys, time



# with open(voice_in_file, 'r') as feed:
#     for i, _ in enumerate(feed):
#         body_len += 1

def digest(voice_in_file):
    # voice_in_file = '.output'
    voice_string = ''
    churn_list = ['']

    with open(voice_in_file, 'r', encoding = 'utf-8', errors= 'ignore') as feed:
        print('feed is formatted %s' % feed.encoding)
        for line in feed:
            if not voice_string:
                voice_string = line
            else:
                churn_list.append(line)

    with open(voice_in_file, 'w') as feed_out:
        for line in churn_list:
            feed_out.write(line)

    for word in voice_string.split(' '):
        if word:
            try:
                with open('.vocab/' + word[0], 'a') as catagory:
                    catagory.write(word +' ')
            except OSError:
                print ('%sis a no no' % word[0])
                with open('.vocab/etc','a') as catagory:
                    catagory.write(word+' ')

while True:
        time.sleep(120)
        print('going now')
        digest('.output')