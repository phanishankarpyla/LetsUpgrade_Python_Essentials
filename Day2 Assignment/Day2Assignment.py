## List and its functions: 
List1=["Hello",22,"Pyla Phani Shankar",1998,8.98];
List1.append(21);
List1.insert(0,"Welcome");
List1.reverse();
List1.remove("Hello");
List1.count(22);
List1.clear();
print(List1)

## Dictionary and its functions
Dict1={"Name":"Phani","Bill.No":1234521,"Orders":"Pizza","Total_Amount":255}
b=Dict1.get("Name"); print(b);
c=Dict1.items(); print(c); 
Dict1.pop("Orders");
Dict1.update({"New":"Nothing"});
Dict1.popitem() ## last element is removed
d=Dict1.setdefault("Name"); print(d);
e=Dict1.values(); print(e);
Dict1.clear();
print(Dict1);

# Sets and its functions
Set1={"Name",21,20,54,"phani",52.21,2,1,2,1,2,2};
Set2={2,1,2,5,4,2,54,2,1,41,51};
Set1.add("Shankar");
f=Set2.difference(Set1); print(f);
g=Set1.intersection(Set2);print(g);
h=Set2.issubset(Set2);print(h);
i=Set1.union(Set2);print(i);
j=Set1.symmetric_difference(Set2);print(j);
Set1.clear();
print(Set1);

# Tuple and its functions
Tup1=(21,"Phani",54,22,21.215);
k=Tup1.count(21);print(k);
l=Tup1.index(22);print(l);
m=type(Tup1[2]);print(m);
print(Tup1); #we cannot perform much fuctions on Tuple as it is Immutable

#String and some operations
Name="Pyla Phani Shankar";
print(type(Name));
print(Name[11]);
print(Name.index("S"))
print(Name,"Allu");
print(Name.upper());
print(Name.count("P"));
Name2="Allu";
Full=Name+" "+Name2;
print(Full);