from flask import Flask, request, render_template, redirect, url_for
import requests
from twilio.twiml.messaging_response import MessagingResponse
from urllib.request import urlopen as myRequest
import os
import wikipediaapi
import randfacts
from datetime import datetime
import datetime

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return redirect('http://www.mdcallianceparty.org')

@app.route('/bot', methods = ['POST', 'GET'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False

    media_number = int(request.values['NumMedia'])
    media = request.values.get('MediaContentType0', '')

    user_cell = request.values['From']
    user_profile = request.values['ProfileName']

    base_url = 'https://www.mdcallianceparty.org'
    

    if 'hi' in incoming_msg:
    	reply = (f"Hello {user_profile}, I am Vote263 Bot :). I am here to help you with Zimbabwe's hot Harmonised Elections 2023 Information. \n"
                    "\n"
                    "Type a word or number from the menu to get more infomation. For example 'Why' or '2' \n"
                    "\n"
                    "*>> Why:* Read on *WHY* you must vote.\n"
                    "\n"
                    "*>> 1 :* How to register to vote.\n"
                    "\n"
                    "*>> 2 :* Where to Register to Vote.\n"
                    "\n"
                    "*>> 3 :* Check your registration on BVR website. \n"
                    "\n"
                    "*>> 4 :* Frequently Asked Questions. \n"
                    "\n"
                    "*>> 5 :* Downloads. \n"
                    "\n"
                    "*>> 6:* Wiki. Get information from Wikipedia. \n "
                    "\n"
                    "*>> 7:* MDC Alliance WhatsApp portal.\n "
                    "\n"
                    "*>> News :* Get the Global News.\n"
                    "\n"
                    "*>> Corruption :* Resources on Corruption in Zimbabwe & Africa.\n"
                    "\n"
                    "*>> Resources :* More resources (coming soon).\n"
                    "\n"
                    "*>> Quotes :* Free quotes on Politics, Science, Life & Happiness.\n"
                    "\n")
    	msg.body(reply)
    	responded=True


    if incoming_msg == 'why':
        reply = (f"Why it is important to register to vote. From Kubata.net Website. \n"
                    "\n"
                    "*>>* An individual’s right to vote ties that person to our social order, even if that person chooses not to exercise that right. \n"
                    "\n"
                    "*>>* Voting represents the beginning; everything else in our democracy follows the right to vote. Participation is more than just a value. It is a foundational virtue of our democracy.\n"
                    "\n"
                    "Follow this link for more: https://kubatana.net/2020/11/19/the-importance-of-voter-registration-to-the-youth/ \n"
                    "\n"
                    "*>> Hi :* Main Menu"
                    "\n")
        msg.body(reply)
        responded=True

    if incoming_msg == '5':
    	reply = (f" *Download important files.* \n"
                    "\n"
                    "*>> 2018 Harmonised Election Report.* \n Click link to Download. \n https://drive.google.com/file/d/1G8soxOjsy90Kqz1gWLK_HSuHVzUHCbrF/view?usp=sharing \n"
                    " \n "
                    "*>> The Curse Of Corruption In Zimbabwe - Thabani Nyoni - University of Zimbabwe.* \n Click link to Download. \n https://drive.google.com/file/d/1qv9KvmPz-yUQgN3iIygfbT0zN2DPx6D9/view?usp=sharing \n "
                    "\n"
                    "*>> Shadows and Shell Games - Uncovering an Offshore Business Empire in Zimbabwe* \n https://drive.google.com/file/d/1KZ9C_pBRanZ87gFoTaEJcfM52qGhYXdV/view?usp=sharing \n "
                    "\n"
                    "*>> ZEC Strategic Plan 2019-2024* \n https://drive.google.com/file/d/1VZrbxSKnqVenpUCgswrTktzeebXJdS-n/view?usp=sharing \n"
                    "\n")
    	msg.body(reply)
    	responded=True


    elif incoming_msg == '2':
        reply = (f"{user_profile}, here is the provinces list. Type province initials eg BM to get the nearest addresse to register to vote. \n"
                    "\n"
                    "*>> BM :* Bulawayo Metropolitan. \n "
                    "\n"
                    "*>> HM :* Harare Metropolitan .\n"
                    "\n"
                    "*>> MR :* Manicaland.\n"
                    "\n"
                    "*>> MC :* Mashonaland Central. \n"
                    "\n"
                    "*>> ME :* Mashonaland East.\n"
                    "\n"
                    "*>> MW :* Mashonaland West.\n"
                    "\n"
                    "*>> MO :* Masvingo.\n"
                    "\n"
                    "*>> MD :* Midlands.\n"
                    "\n"
                    "*>> MN :* Matabeleland North.\n"
                    "\n"
                    "*>> MN :* Matabeleland South.\n"

                    "\n"
                    "*>> Hi :* Main Menu"
                    "\n")
        msg.body(reply)
        responded=True

    if  incoming_msg == '3':
        # return a cat pic
        reply = (f"Click on the link below to find out if you are registered. Make sure you have your ID Number with you. \n"
                    "\n"  
                    f"https://bvrinspection.zec.org.zw/ \n"
                     "\n"
                    "*>> Hi :* Main Menu"                
                    "\n")
        msg.body(reply)
        responded = True

    if  incoming_msg == 'bm':
        # return a cat pic
        reply = (f"{user_profile}, here are the voting places in Bulawayo Metropolitan. \n"
                    "\n"
                    "*>> Bulawayo :* 14 Centenary Court, Windsor Park, Building 16th Avenue, Famona Bulawayo.\n"
                    "\n"
                    "*>> Bulawayo :* 18 Rylanders Court, Windsor Park, Complex,16th Avenue, Famona, Bulawayo.\n"                 
                     "\n"
                    "*>> Hi :* Main Menu"
                    "\n")
        msg.body(reply)
        responded = True

    if  incoming_msg == 'hm':
        # return a cat pic
        reply = (f"*Here are the voting places in Harare Metropolitan. *\n"
                    "\n"
                    "*>> Harare :* 95 Jason Moyo Avenue, 4th Floor, Cecil House Harare.\n"
                    "\n"
                    "*>> Harare :* Rememberance Complex, No. 2, Rememberence Drive, Mbare, Harare.\n"
                    "\n"
                    "*>> Chitungwiza :* Seke Teachers’ College, Stand No. 16120, Mangwende Drive, Chitungwiza.\n"
                    
 					 "\n"
                    "*>> Hi :* Main Menu"
                    
                    "\n")
        msg.body(reply)
        responded = True

    if  incoming_msg == 'mr':
        # return a cat pic
        reply = (f"Here are the voting places in Manicaland. \n"
                    "\n"
                    "*>> Mutare :* 1st Floor New Government Complex, Cnr Robert Mugabe and 4th Street Mutare.\n"
                    "\n"
                    "*>> Buhera :* Buhera Rural District Council Offices, Murambinda, Buhera.\n"
                    "\n"
                    "*>>Chipinge :* New Government Complex, Block B 2nd floor, Chipinge.\n"
                    "\n"
                    "*>>Makoni :* District Administrator’s Complex, Chingaira Building, Rusape.\n"
                    "\n"
                    "*>> Mutare :* District Administrator’s Complex, 43 Tembwe Street, Mutare.\n"
                    "\n"
                    "*>> Mutasa :* DC Mutasa Messenger’s Camp, Stand No. 4894,Mutasa.\n"
                    "\n"
                    "*>> Nyanga :* District Administrator’s Complex, Nyanga.\n"
                    "\n"
                    "*>> Nyanga :* District Administrator’s Complex, Nyanga.\n"
                     "\n"
                    "*>> Hi :* Main Menu"
               
                    "\n")
        msg.body(reply)
        responded = True

    if  incoming_msg == 'mc':
        # return a cat pic
        reply = (f"*Here are the voting places in Mashonaland Central. *\n"
                    "\n"
                    "*>> Bindura :* 2nd Floor Mtungagore Building, Bindura.\n"
                    "\n"
                    "*>> Bindura :* Mutungagore Building, Office No. G73, Bindura.\n"
                    "\n"
                    "*>>Guruve :* Old Magistrate Court, District Administrator’s Complex, Guruve.\n"
                    "\n"
                    "*>>Mazowe :* District Administrator’s Complex, Concession, Mazowe.\n"
                    "\n"
                    "*>>Mbire :* Mbire Rural District Council Offices, Mbire.\n"
                    "\n"
                    "*>>Mount Darwin :* District Administrator’s Complex, Office No. 27,Mount Darwin.\n"
                    "\n"
                    "*>>Muzarabani :* Palmwal Agencies Building, Stand No. 145, Centenary.\n"
                    "\n"
                    "*>>Rushinga:* District Administrator’s Complex, Office No. 14,Rushinga.\n"
                    "\n"
                    "*>>Shamva :* Stand No. 203,Main Street, Shamva.\n"
                     "\n"
                    "*]*>> Hi :* Main Menu"
                    
                    "\n")
        msg.body(reply)
        responded = True

  
    if  incoming_msg == 'me':
        # return a cat pic
        reply = (f"*Here are the voting places in Mashonaland East.* \n"
                    "\n"
                    "*>> Marondera :* 2 Fifth Street, Marondera.\n"
                    "\n"
                    "*>> Chikomba :*  58 Main Street Chivhu.\n"
                    "\n"
                    "*>> Goromonzi :* Public Works Complex, Goromonzi.\n"
                    "\n"
                    "*>> Marondera :* District Administrator’s Office, No. 1 First Street,Marondera.\n"
                    "\n"
                    "*>> Mudzi :*  Government Complex, Kotwa Growth Point, Mudzi.\n"
                     "\n"
                    "*>> Hi :* Main Menu"
                    "\n")
        msg.body(reply)
        responded = True
 
    if  incoming_msg == 'mw':
        # return a cat pic
        reply = (f"*Here are the voting places in Mashonaland West. *\n"
                    "\n"
                    "*>> Chinhoyi :* 8 Robson Manyika Drive, Chinhoyi.\n"
                     "\n"
                    "*>> Hi :* Main Menu"
                    "\n")
        msg.body(reply)
        responded = True

    if  incoming_msg == 'mo':
        # return a cat pic
        reply = (f"Here are the voting places in Masvingo. \n"
                    "\n"
                    "*>> Masvingo :* 10 Hellet Street, Masvingo.\n"
                     "\n"
                    "*>> Hi :* Main Menu"
                    "\n")
        msg.body(reply)
        responded = True

    if  incoming_msg == 'md':
        # return a cat pic
        reply = (f"Here are the voting places in Midlands. \n"
                    "\n"
                    "*>> Gweru :* 10th Street, Ground Floor, Government Complex, Gweru.\n"
                     "\n"
                    "*>> Hi :* Main Menu"
                    "\n")
        msg.body(reply)
        responded = True

    if  incoming_msg == 'mn':
        # return a cat pic
        reply = (f"Here are the voting places in Matabeleland North. \n"
                    "\n"
                    "*>> Bulawayo :* 10-12 Centenary Court, Windsor, Park Building 16th Avenue, Famona, Bulawayo.\n"
                     "\n"
                    "*>> Hi :* Main Menu"
                    "\n")
        msg.body(reply)
        responded = True


    if  incoming_msg == 'ms':
        # return a cat pic
        reply = (f"Here are the voting places in Matabeleland South. \n"
                    "\n"
                    "*>> Gwanda :* 1194 Bigben Road, Jahunda, Gwanda.\n"
                     "\n"
                    "*>> Hi :* Main Menu"
                    "\n")
        msg.body(reply)
        responded = True

    if  incoming_msg == '4':
        reply = (f" *Zimbabwe Electoral Commission - Frequently Asked Questions.* \n"
                    "\n"
                    "*1. On Election Day will the BVR machine be there to verify a voter's finger prints?* \n"
                    "\n"
                    "Answer: On polling day the BVR machine will not be there. The Commission will make use of a person’s identity document and the picture taken during voter registration. Polling Officers will not inspect a person’s finger prints.\n"
                    "\n"
					"\n"
                    "*2. May we be given a chance to cast our votes through postal voting since the majority of us will be posted elsewhere as polling officers?* \n"
                    "\n"
                    "*Answer:* Section 72(a) of the Electoral Act allows electoral officers deployed outside their areas of voting to exercise their right to vote by post. However, ZEC does not encourage the deployment of the election officers away from their areas of registration. All efforts will be made to try and deploy polling officers to where they can vote. \n"
                    "\n"
                    "*3. Can I vote anywhere in my ward?* \n"
                    "\n"
                    "*Answer:* This year’s elections are polling station based as such one’s name appears on a single polling station. This makes it impossible for a person to cast their vote at any other polling station besides the one allocated during registration to vote. \n"
                    "\n"
                    "*4. How do blind people vote?* \n"
                    "\n"
                    "Answer: They will be assisted by a person of their own choice who should be 18 years and above.\n"
                    "\n"

                    "*>> Hi :* Main Menu"
                    "\n")
        msg.body(reply)
        responded = True


    if '1' in incoming_msg:
        # return a quote
        quote = ("*How to register vote in Zimbabwe 2023 Harmonised Elections.* \n"
"\n"
        	"*Documents required for:* \n"
"\n"
" *1. Registration* \n"
"\n"
 " *>>* National Identity Card (metal, plastic or waiting pass with holder’s picture) or Valid Zimbabwean passport  \n"
"  *>>* Proof of residence (For those who cannot produce proof of residence, anaffidavit is available at the Registration)\n"
"\n"
" *2. Inspection* \n"
"\n"
 " *>>* National Identity Card (metal, plastic or waiting pass with holder’s picture) or Valid Zimbabwean passport\n"
"  *>>* Proof of residence (For those who cannot produce proof of residence, an affidavit is available at the Registration)\n"
"\n"
" *3. Transfer* \n"
"\n"
" *>>* National Identity Card (metal, plastic or waiting pass with holder’s picture) or Valid Zimbabwean passport \n"
"*>>* Proof of residence or affidavit\n"
"\n"
"NB ZEC will advise the public when registration resumes. The Commission is currently waiting for the alignment of the electoral Act to the Constitution. Any queries can be directed to the Zimbabwe Electoral Commission provincial or district offices located in each respective province or district. \n"
"\n"  
"*>> Hi :* Main Menu"
 "\n"
                    
                    )   
        msg.body(quote)
        responded = True

    if incoming_msg == '7':
        html_page = myRequest(base_url + '/membership-plans/')
        reply = (f"{user_profile}, welcome to the MDC Alliance Portal. \n"
                    
                    "\n"
                    "*>> Web: MDC official Website  \n"
                    "\n"
                    "*>> MDCNews :* MDC Alliance News.\n"
                    "\n"
                    "*>> Donate :* Donate To The MDC Alliance. \n"
                    "\n"
                    "*>> Subs :* Monthly Subscription.\n"
                    "\n"
                    "*>> Join :* Become A Member.\n"
                    "\n"
                    "*>> Contact:* Contacts. \n"
                    "\n"
                    "*>> Hi :* Main Menu"
                    "\n")
        msg.body(reply)
        responded=True


    if  incoming_msg == 'web':
        # return a cat pic
        reply = (f"Click on the link below to go to the Official Home Page. \n"
                    "\n"
                    "https://www.mdcallianceparty.org.\n"
                     "\n"
                    "*>> Hi :* Main Menu"
                    "\n")
        msg.body(reply)
        responded = True

    if  incoming_msg == 'mdcnews':
        # return a cat pic
        reply = (f"Click on the link below to go to the Official News Page. \n"
                    "\n"
                    "https://www.mdcallianceparty.org/news/.\n"
                     "\n"
                    "*>> Hi :* Main Menu"
                    "\n")
        msg.body(reply)
        responded = True

    if  incoming_msg == 'donate':
        # return a cat pic
        reply = (f"Click on the link below to go to the Official Donations Page. \n"
                    "\n"
                    "https://payments.mdcallianceparty.org/#/donations.\n"
                     "\n"
                    "*>> Hi :* Main Menu"
                    "\n")
        msg.body(reply)
        responded = True

    if  incoming_msg == 'subs':
        # return a cat pic
        reply = (f"Click on the link below to go to the Official Donations Page. \n"
                    "\n"
                    "https://payments.mdcallianceparty.org/#/memberSubscriptions.\n"
                     "\n"
                    "*>> Hi :* Main Menu"
                    "\n")
        msg.body(reply)
        responded = True

    
    if  incoming_msg == 'join':
        # return a cat pic
        reply = (f"Click on the link below to go to the Official Joining Page. \n"
                    "\n"
                    "https://www.mdcallianceparty.org/membership-plans/.\n"
                     "\n"
                    "*>> Hi :* Main Menu"
                    "\n")
        msg.body(reply)
        responded = True


    if  incoming_msg == '6':
        # return a cat pic
        reply = (f"Type Wiki then search word \n"
                    "\n"
                    "For example 'wiki politics' or 'wiki zimbabwe' or 'wiki democracy' or 'wiki corruption' \n"
                    "*>> Hi :* Main Menu"
                    "\n")
        msg.body(reply)
        responded = True


    if  incoming_msg == 'contacts':
        # return a cat pic
        reply = (f"* Contacts *. \n"
                    "\n"
                    "Phone: +263 772 233872.\n"
                    "\n"
                    "WhatsApp: +263 772 233872.\n"
                    "\n"
                    "info@mdcallianceparty.org.\n"


                     "\n"
                    "*>> Hi :* Main Menu"
                    "\n")
        msg.body(reply)
        responded = True

    

    if incoming_msg == 'news':
        r = requests.get('https://newsapi.org/v2/everything?q=politics&apiKey=0b38960d9e474d74a228b66e214eb682')
            
        if r.status_code == 200:
            data = r.json()
            articles = data['articles'][:5]
            result = ''
            
            for article in articles:
                title = article['title']
                url = article['url']
                if 'Z' in article['publishedAt']:
                    published_at = datetime.datetime.strptime(article['publishedAt'][:19], "%Y-%m-%dT%H:%M:%S")
                else:
                    published_at = datetime.datetime.strptime(article['publishedAt'], "%Y-%m-%dT%H:%M:%S%z")
                result += """
    *{}*
    Read more: {}
    _Published on {:02}/{:02}/{:02} @ {:02}:{:02} UTC_
    """.format(
    title,
    url, 
    published_at.day, 
    published_at.month, 
    published_at.year, 
    published_at.hour, 
    published_at.minute, 
    published_at.second
    )

        else:
            result = 'I cannot fetch news at this time. Sorry!'

        msg.body(result)
        responded = True

    if 'wiki' in incoming_msg:
        #! Returning summary from wikipedia
        query = incoming_msg.replace('wiki ', '')
        wiki = wikipediaapi.Wikipedia('en')
        try:
            page = wiki.page(query)
            url = page.fullurl
            summary = page.summary[0:1500]
            msg.body(f"According to wikipedia..\n\n{summary}...\n{url}\n")
        except:
            msg.body("Sorry can't find anything.\nTry another search..")


    if incoming_msg == 'quote':
            # returns a quote
            r = requests.get('https://api.quotable.io/random?tags=politics|love|hapiness|science|life')

            if r.status_code == 200:
                data = r.json()
                quote = f'{data["content"]} \n \n ~ {data["author"]}'

            else:
                quote = 'I could not retrieve a quote at this time, sorry.'

            msg.body(quote)
            responded = True


    if  incoming_msg == 'corruption':
        # return a cat pic
        reply = (f" *>> Click on the links below to learn more about Corruption in Africa* \n"
                    "\n"
                    " *Wikipedia* - Corruption in Zimbabwe has become endemic within its political, private and civil sectors. Zimbabwe ranks joint 160th out of 180 countries in the 2016 Transparency International Corruption Perceptions Index. On a scale of 0 (highly corrupt) to 100 (very clean), the Corruption Perceptions Index marked Zimbabwe 22. This marks an increase in corruption since 1999, when the country ranked 4.1 (out of ten). Source: https://en.wikipedia.org/wiki/Corruption_in_Zimbabwe.\n"
                     "\n"
                     " *>> Zimbabwe Corruption Report - Last updated: May 2020* \n"
                     "Across all sectors, corruption is a very high risk for companies operating in Zimbabwe. Investors face both high-level corruption in the form of nepotism, patronage and abuse of power, as well as petty bribery and extortion. The Prevention of Corruption Act prohibits active and passive bribery, gifts and facilitation payments in the public and private sectors, but such practices are common. Companies can be held criminally liable. Source: https://www.ganintegrity.com/portal/country-profiles/zimbabwe/ \n "
                     "\n"
                     #" *Exploring the role of illicit financial flows in Zimbabwe’s political economy* Mail & Guardian Article \n"
                     #"This Good Governance Africa webinar was hosted by the Mail & Guardian. It featured as speakers Honourable Tendai Biti, Former Finance Minister during Zimbabwe’s coalition  government  2009-2013; Mark Heywood, Human Rights and Social Justice Activist; Farai Maguwu, Founder of the Centre for Natural Resource Governance; Professor Francis Gudyanga, Founding Fellow and past President of the Zimbabwe Academy of Sciences... https://mg.co.za/special-reports/2021-05-27-exploring-the-role-of-illicit-financial-flows-in-zimbabwes-political-economy/ \n"
                     # "\n"
                     # " *Sentry Report Reveals Hidden Business Practices of Zimbabwean Tycoon Kudakwashe Tagwirei* \n"
                     # "July 1, 2021 (Washington, DC) – A report published today by The Sentry, “Shadows and Shell Games: Uncovering an Offshore Business Empire in Zimbabwe,” reveals key details of the business practices of controversial businessman and presidential advisor Kudakwashe Tagwirei. The Sentry’s investigation reveals that Tagwirei, who has been followed by allegations of corruption and cronyism for years, has been using complex corporate structures and seemingly preferential government treatment to build his business empire and enormous wealth. https://thesentry.org/2021/07/01/6155/breaking-sentry-report-reveals-hidden-business-practices-zimbabwean-tycoon-kudakwashe-tagwirei/ \n"
                     # "\n"
                     # " *The offshore hive of Zimbabwe’s ‘Queen Bee’* \n"
                     # "As ruthless, army-backed successor to Robert Mugabe, Zimbabwe’s President Emmerson Mnangagwa is known as the crocodile. And yet the best symbol of how hopes for a better Zimbabwe have faded since the 2017 coup against Mugabe is, in many ways, a bee. After he took power, Mnangagwa promised to make Zimbabwe “open for business” and to end systematic corruption that obliterated the economy under the late dictator. https://www.ft.com/content/af8f3546-1b9b-40f1-afb1-5e7ce3b011da/ \n"
                     # "\n"
                    

                    "*>> Hi :* Main Menu"
                    "\n")
        msg.body(reply)
        responded = True



    if  incoming_msg == 'webs':
        # def red():
        #     return render_template('officialmdc.html')
        def index1():
            return """<html><body>
                    Redirecting to MDC Alliance Website...
                    </body>
                    <script>
                       function myFunction() {
                       location.replace("https://www.mdcallianceparty.org")
                       }

                       setTimeout(function(){ myFunction(); }, 3000);
                    </script>
                    </html>
                    """


        reply = index1()

        msg.body(index1())
        responded = True


    # if not responded:
    #      msg.body('I only know about famous quotes and cats, sorry!')

    return str(resp)


if __name__ == '__main__':
    app.run(debug=True)
    port = int(os.environ.get('PORT', 5000))
    # app.run()