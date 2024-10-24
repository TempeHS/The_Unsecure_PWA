# Time based information leak

This example side channel exploits a time-based information leak vulnerability. The exploit can enumerate if a username is valid by analysing the different response times for a valid versus invalid username. The threat actor would use datasets from data breaches, with the now verified usernames, to perform a more targeted dictionary attack informed by the corresponding known previous passwords.

> [!Note]
> Students are not expected to be able to duplicate this application or understand the complex Python implementation. This example is to model how information can leak and then be exploited only.

## Requirements

```bash
pip install requests
pip install matplotlib
pip install rich
```

## Demonstration

### Step 1: Setup

The app needs to be running on port 5000 and the list of usernames to test are in [users.txt](users.txt).

### Step 2: Analysis of time differences between valid and invalid usernames

First step is to analyze whether there is a time based leak of information on the login tries:

```python
python TimeBasedLoginAnalysis.py -u admin -S
```

![An example graph output of the time analysis](README_Resources/graph.png)

### Step 3: Enumerate usernames based on response times

Now that we know that there is a time based leak of information, we can enumerate users with this command:

```python
python TimeBasedLoginUserEnum.py -u admin -t 32 -s 100 -f users.txt
```

![An example username validation](README_Resources/example.png)
