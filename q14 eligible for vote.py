def eligible_for_vote(age):
    if age<18:
        print("not eligible")
    else:
        print("eligible for vote")
eligible_for_vote(age=int(input("enter the age")))