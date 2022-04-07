Navigate to the working directory

### Install the required framework and libraries
Install python and virtual environment
```
sudo pip install virtualenv
brew install python
virtualenv -p python3 <env_name>
source <env_name>/bin/activate
```

Install the required libraries
```
pip install -r requirements.txt
```
### Running the Tests
python test_full_functionality.py

### Notes

When setting up a framework, please note the following:

1. I would use Page Object Model. Under this, all the locators would be kept in a separate file. This would ensure that  the locators can be easily located and updated, if required. Also, they are declared only once and used wherever they are needed.
2. I would not ued absolute x-path (for ex. line 56 in  test_full_functionality) as they are prone to breaking. I would insert data-test-id attribute and use it to get more stable locators.
3. Login, Logout and other common and repetitive functionalities would be created in a separated file and called whereever required.
4. All the user information like login credentials would be stored in some sort of json file.
5. Test data would be stored in an excel file.
6. Also, for clearing the test data, I would prefer API calls rather than deleting on the front end.
