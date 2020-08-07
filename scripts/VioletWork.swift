import Foundation

var str = "Hello, playground"

func helloName( name: String) -> String {

    let greeting = ("Hello, (name)!")
    print(greeting)

    return greeting
}

helloName("Violet")
helloName("Eyvonne")
helloName("Milou")

/*
 Create a function that accepts a string, checks if it's a valid email address and returns either true or false, depending on the evaluation.
 
 The string must contain an @ character.
 The string must contain a . character.
 The @ must have at least one character in front of it.
 e.g. "e@edabit.com" is valid while "@edabit.com" is invalid.
 The . and the @ must be in the appropriate places.
 e.g. "hello.email@com" is invalid while "john.smith@email.com" is valid.
 */


//func validateEmail( str: String) -> Bool {
//
//    switch str :
//
//    case
//
//
//    return true
//}

func convert( minutes: Int) -> Int {

    let seconds = minutes * 60
    print(seconds)

    return seconds

}

convert(1)
convert(2)
convert(5)


func addition( num: Int) -> Int {

    let newNum = num + 1
    print(newNum)

    return newNum

}

addition(12)
addition(25)


//Given two strings, firstName and lastName, return a single string in the format "last, first".


func concatName( firstName: String,  lastName: String) -> String {

    let lastFirst = lastName + "," + " " + firstName
    print(lastFirst)

    return lastFirst

}


concatName("Violet", "Love")
concatName("Eyvonne", "Geordan")



//Create a function that takes an array of two numbers and checks if the square root of the first number is equal to the cube root of the second number.

func checkSquareAndCube(_ array: [Int]) -> Bool {
    let num_1 = Double(array[0])
    let num_2 = Double(array[1])

    if sqrt(num_1) == cbrt(num_2) {

        return true

    } else {

        return false

    }
}
checkSquareAndCube([6,9])