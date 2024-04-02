banner=r"""

██████╗  █████╗ ██████╗  █████╗ ███╗   ███╗      ██████╗ ██╗      █████╗ ███████╗████████╗███████╗██████╗ 
██╔══██╗██╔══██╗██╔══██╗██╔══██╗████╗ ████║      ██╔══██╗██║     ██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██████╔╝███████║██████╔╝███████║██╔████╔██║█████╗██████╔╝██║     ███████║███████╗   ██║   █████╗  ██████╔╝
██╔═══╝ ██╔══██║██╔══██╗██╔══██║██║╚██╔╝██║╚════╝██╔══██╗██║     ██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
██║     ██║  ██║██║  ██║██║  ██║██║ ╚═╝ ██║      ██████╔╝███████╗██║  ██║███████║   ██║   ███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝                                                                                                                                                                                                   
                                                       by Abhishek Dirisipo
"""
print(banner)

red_color = "\033[91m"
magenta_color = "\033[95m"
cyan_color = "\033[96m"
white_color = "\033[97m"
reset_color = "\033[0m"
yellow_color="\033[93m"
clear_line = "\033[K"

import glob

print(yellow_color+"\nList of All text Files in Current Directory:\n"+white_color)
file_count=0
for file in glob.glob("input/with_param/*.txt") :
    file_count+=1
    print(file_count,file)
for file in glob.glob("input/no_param/*.txt") :
    file_count+=1
    print(file_count,file)
for file in glob.glob("input/*.txt") :
    file_count+=1
    print(file_count,file)
for file in glob.glob("*.txt") :
    file_count+=1
    print(file_count,file)

file_count2=input(cyan_color+"✨Enter File Number:  - ")

#********** function for file selecting through serial number *****
def fcount(file_count2):
    file_count=0
    for file in glob.glob("input/with_param/*.txt"):
        file_count+=1
        if file_count==file_count2:
            return file
            
    for file in glob.glob("input/no_param/*.txt"):
        file_count+=1
        if file_count==file_count2:
            return file
                        #1
    for file in glob.glob("input/*.txt"):
        file_count+=1
        if file_count==file_count2:
            return file
                        #2
    for file in glob.glob("*.txt"):
        file_count+=1
        if file_count==file_count2:
            return file
#*******************************************************************
fn=fcount(int(file_count2))
print(red_color+"\nselected file: ",yellow_color+fn)
#***** 
unique_urls = set()  


# Write unique URLs to a file

unique_url_file="logs/unique_urls/"+fn.replace("input/","")

try:
    with open("logs/unique_urls/"+fn.replace("input/",""),'r') as ID1:
        #unique_urls=ID1.readlines()
        print("💾 previous scan urls found !")
except:


    with open(fn) as raw_urls:
        for raw_url in raw_urls:
            # Remove leading and trailing whitespace
            raw_url = raw_url.strip()
            
            # Split the URL at the first occurrence of "?"
            url_without_params = raw_url.split('?')[0]
            
            unique_urls.add(url_without_params)
            #print(url_without_params)

    with open(unique_url_file, "w") as output_file:
        for url in unique_urls:
            output_file.write(url + '\n')


        
unique_urls=set() # clear set
value1="abhi"
value2="\"abhi<>%27<>%3F~!%23$^%26*()_+-=[]{},.@%"

user_in=input("1.abhi\n2.\"abhi<>%27%3F~!%23$^%26*()_+-=[]{},.@%\n3.\"abhi<>'\nEnter Mode:")
if user_in==1:
    value2="abhi"
if user_in==2:
    value2="\"abhi<>%27%3F~!%23$^%26*()_+-=[]{},.@%"
if user_in==3:
    value2="\"abhi<>'"
else:
    value2="\"abhi<>%27%3F~!%23$^%26*()_+-=[]{},.@%"
    







import re
import requests
import time

#-------------- resuming - dont touch any variables - abhishek dirisipo : ) --------------
def extract_file_name(file_path):
    pattern = r'.*/([^/]+)\.txt$'
    match = re.match(pattern, file_path)
    if match:
        return match.group(1)
    else:
        return None

file_name = extract_file_name(fn)

try:
    with open('logs/resume_stats/'+file_name,'r') as ID1:
        temp=ID1.readline()
        resume_count=int(temp)
        print("💾 previous task has being resumed ...")
except:
    with open('logs/resume_stats/'+file_name,'w') as ID1:
        ID1.write("0")
        resume_count=0
#-----------------------------------------------------

def count_symbols(response_text, symbols):
    symbol_counts = {}
    total_count = 0
    for symbol in symbols:
        count = response_text.count(symbol)
        symbol_counts[symbol] = count
        total_count += count
    symbol_counts['total'] = total_count
    return symbol_counts

time_delay=0

def fire_params(url_with_param,value_received,time_delay):

    try:
       
        response = requests.get(url_with_param)
        response_text = response.text
        response_text=response_text.lower()
        content_type = response.headers.get('Content-Type')

        #if value_received!="abhi":
        symbols_count = count_symbols(response_text, symbols)
        symbols_total_count=symbols_count['total']
        reflections_count=response_text.count("abhi")
        
        if "429" in str(response.status_code):
            print(".. maintaining delay for 1 min for now and incrementing 1 sec delay for each")
            time.sleep(60)
            time_delay=time_delay+1
            
        if "\"abhi<>" in response_text and content_type and 'html' in content_type:
            with open("logs/xsslogs-1.txt", 'a') as log_file:
                log_file.write(url_with_param+ "\n")
        
        return symbols_total_count,reflections_count,response.status_code,len(response_text),time_delay

            
    except requests.RequestException as e:
        print("Error sending request to", url)

def write_log(string, fn):
    # Define the regular expression pattern to match color codes
    color_pattern = re.compile(r'\x1b\[[0-9;]*m')
    # Remove color codes from the string
    cleaned_string = re.sub(color_pattern, '', string)
    # Write the cleaned string to the log file
    with open("logs/" + fn.replace("input/", ''), 'a') as log_file:
        log_file.write(cleaned_string + "\n")

def write_log_filtered(string, fn):
    # Define the regular expression pattern to match color codes
    color_pattern = re.compile(r'\x1b\[[0-9;]*m')
    # Remove color codes from the string
    cleaned_string = re.sub(color_pattern, '', string)
    # Write the cleaned string to the log file
    with open("logs/results/" + fn.replace("input/", ''), 'a') as log_file:
        log_file.write(cleaned_string + "\n")

def save_count(file_name,url_count):
    with open('logs/resume_stats/'+file_name,'w') as ID1:
        ID1.write(str(url_count))

def extract_parameters(response_text):
    # Regular expression pattern to match parameter names in the query string
    pattern = r'[\?&]([^=]{1,' + str(10) + '})='

    # Find all matches of the pattern in the response text
    matches = re.findall(pattern, response_text)

    # Remove duplicate parameter names by converting the list to a set
    parameters = list(set(matches))

    return parameters



symbols = '"<>\'?~!@#$%^&*()_+-=[]{},.'

url_count=0


with open(unique_url_file) as unique_urls:
    for unique_url in unique_urls:
        url_count += 1
        if url_count < resume_count :
            print("skipping"+str(resume_count)+":"+str(url_count))
            continue
        unique_url=unique_url.strip()
        unique_url_with_fake_param1=unique_url+"?fparam="+value1
        unique_url_with_fake_param2=unique_url+"?fparam="+value2

        static_extensions = [".js?", ".jpg", ".jpeg", ".png", ".gif", ".css", ".ico", ".woff", ".woff2", ".ttf", ".otf", ".svg", ".eot"]
        
        if any(ext in unique_url_with_fake_param1 for ext in static_extensions):
            print(" skipping static files/pages")
            save_count(file_name,url_count)
            continue


        try:
            #print("1."+unique_url_with_fake_param1)
            #response1 = requests.get(unique_url_with_fake_param1)
            #response_text1=response1.text
            #response_text1=response_text1.lower()

            print(str(url_count)+" [Main]:"+unique_url_with_fake_param2)
            
            time.sleep(time_delay) # delay time before request
            response1=response2 = requests.get(unique_url_with_fake_param2)
            response_text2=response2.text
            response_text1=response_text2=response_text2.lower()
            
            if response1.status_code ==403:
                print(" forbidden , skipping")
                save_count(file_name,url_count)
                continue
            if response1.status_code ==404:
                print(" Not found , skipping")
                save_count(file_name,url_count)
                continue


            parameters_in_page = extract_parameters(response_text1)
            
            if  "429" not in str(response1.status_code):

                initial_status_code1=response1.status_code
                initial_status_code2=response2.status_code
                
                initial_reflections_count=response_text1.count("abhi")
                
                
                initial_symbols_count = count_symbols(response_text2, symbols)
                initial_symbols_total_count=initial_symbols_count['total']

                
                string_to_write3=(red_color + "--> fake abhi counts:" + yellow_color + str(initial_reflections_count) +
                      red_color + " st:" + reset_color + yellow_color + str(initial_status_code1) +
                      red_color + "  fake symbols count:" + yellow_color + str(initial_symbols_total_count) +
                      red_color + " Len:" + reset_color + yellow_color + str(len(response_text2)))
                print(string_to_write3)
                #write_log(string_to_write3,fn)
                #----------------------------------------
                with open("parameters/parameters.txt") as parameters_file:
                    parameters = parameters_file.readlines()
                    parameters_in_page.extend(parameters)

                unique_response_lengths=[]
                
                for parameter in parameters_in_page:
                    parameter=parameter.strip()
                    if any(char in parameter for char in ["fparam", "#", ";", "'", "\"", "�", "&", ",", "(" ,")"]):
                        continue
                        
                    if "?" not in parameter:
                        parameter="?"+parameter+"="
                        
                    #-----------
                    parameter_filtered=parameter.replace("?","").replace("=","")
                    symbols_count_in_param=count_symbols(parameter_filtered, symbols)
                    #-----------                   
                    url_with_param=unique_url+parameter+value2
                    
                    time.sleep(time_delay) # time delay before request
                    
                    try:
                        symbols_total_count,reflections_count,status_code2,response_length2,time_delay=fire_params(url_with_param,value2,time_delay) #firing params here
                        
                    except:
                        write_log_filtered("[ERROR] :"+url_with_param,fn)
                        continue
                    
                    

                    
                    #-----
                    filtered_length=str(response_length2 - (len(parameter_filtered) - 6) * reflections_count)
                    symbols_count_filtered=symbols_total_count - (reflections_count * symbols_count_in_param['total'])
                    #-----
                    string_to_write1=reset_color+"[*]" + url_with_param
                    #write_log(string_to_write1,fn)
                    print(string_to_write1)

                        
                    if (initial_reflections_count != reflections_count) or (initial_status_code1 !=status_code2 or symbols_count_filtered != initial_symbols_total_count) and ( "429" not in str(status_code2) and  "429" not in str(initial_status_code1) ):
                    
                        # smart skipper ------- 
                        unique_response_lengths.append(filtered_length)
                        count = unique_response_lengths.count(filtered_length)
                        if count >= 2 : 
                            continue
                        # --------------------- 
                        
                        string_to_write2=("    abhi counts:" + yellow_color + str(reflections_count) + reset_color + " st:" +yellow_color+ str(status_code2) + "     symbols count:" + yellow_color + str(symbols_total_count - (reflections_count * symbols_count_in_param['total'])) + red_color+" Len:" + filtered_length)              #--------------------------------------
                        #write_log(string_to_write2,fn)
                        print(string_to_write2)
                        write_log_filtered(url_with_param,fn)
                        
                        
            else:
                print("...blocking .. rate limit . maintaining 60 sec delay and incrementing 1 sec delay for each request")
                time.sleep(60)
                time_delay=time_delay+1

   
        except requests.RequestException as e:
            print("Error sending request to", url)
            save_count(file_name,url_count)
            continue
            
        save_count(file_name,url_count)   