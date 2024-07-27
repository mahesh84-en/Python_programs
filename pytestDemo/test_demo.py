

def test_first_program():
    print("mahesh")

#command line commands
# to run the all the tests -- py.test
#to run all the test with status -- py.test -v
#to run all the test with status and log info -- py.test -v -s
#to run the specific file -- py.test test_demo.py -v -s
#how can i run the one test from one file and one test from another file--- py.test -k Creditcard -v -s
#-k stands for method name and -v statnd for more info and -s logs in output
# i want to run only marked(@pytest.mark.smoke) hourly tests--py.test -m
#i want to skip(@pytest.mark.skip) one test
#i want to skip the test but which operation it's performing i want to do like this @pytest.mark.xfail
#fixture concept is executing required methods before our main tests
#yield keyword after the step executes last after complition of actual test
#conftest file should be like conftest only, whenever you thinks the fixtures are using in multiple tests. You have to create like this
#when we are using the same fixture in multiple tests in one file if we declare this in class level. it'll automatically applies to all test under the calss before class name delare mark like beow
# @pytest.mark.usefixtures("browser")
#i want to execute my driver.close() only after execution of all tests in a class
#@pytest.fixture(scope="class")
