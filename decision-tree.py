from sklearn import tree

#Independence variable X: (example) [Hieght, Weight, Age]
X = [[180, 70, 25],[160, 50, 20],[156, 54, 30],[170, 63, 25],[165, 65, 40],[162, 50, 23],[167, 67, 27]]

#Dependence varibale Y: (example) [Gender]
Y = ['male', 'female', 'female', 'male', 'male', 'female', 'male']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

prediction = clf.predict([[163, 55, 27]])

print(prediction)
