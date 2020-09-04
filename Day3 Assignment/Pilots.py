Altitude=input("Enter your current Altitude: ");
Altitude=int(Altitude);
if Altitude<700:
    print("Very low altitude!, Pull up 500ft to avoid a crash!!");
elif Altitude<=1200 and Altitude>=700:
    print("You are Good to Land Safe");
elif Altitude>1200 and Altitude<5000:
    print("High Altitude!! Come down to 1000ft");
elif Altitude>=5000:
    print("Take a Turn Around and Try again");
