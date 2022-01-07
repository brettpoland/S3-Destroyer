import boto3

def remove_all_s3keys():
        s3 = boto3.resource('s3')
        for bucket in s3.buckets.all():
            for key in bucket.objects.all():
                key.delete()

def remove_all_s3buckets():
        s3 = boto3.resource('s3')
        for bucket in s3.buckets.all():
            bucket.delete()
            
def view_buckets():
        s3 = boto3.resource('s3')
        for bucket in s3.buckets.all():
            print (bucket)

def view_keys():
        s3 = boto3.resource('s3')
        for bucket in s3.buckets.all():
            for key in bucket.objects.all():
                print(key.key)

def view_bucketsandkeys():
        s3 = boto3.resource('s3')
        for bucket in s3.buckets.all():
            print(bucket)
            for key in bucket.objects.all():
                print(key.key)
                

def get_menu_choice():
    def print_menu():       
        print(30 * "-", "Options", 30 * "_")
        print ("1. View Buckets")
        print ("2. View Keys")
        print ("3. View Buckets and Keys")
        print ("4. Delete EVERYTHING!!!!! ****WARNING*****")
        print("5. Exit")
        print(80 * "-")

    loop = True
    int_choice = -1

    while loop:       
        print_menu()    
        choice = input("Enter your choice [1-5]: ")

        if choice == '1':
            view_buckets()
            loop = True
        elif choice == '2':
            view_keys()
            loop = True
        elif choice == '3':
            view_bucketsandkeys()
            loop = True
        elif choice == '4':
            remove_all_s3keys()
            remove_all_s3buckets()
            loop = True
        elif choice == '5':
            print("Exiting..")
            loop = False  
        else:
            input("Wrong menu selection. Enter any key to try again..")
    return [choice] 

get_menu_choice()