import git
from git import Repo

PATH_OF_GIT_REPO = r'C:\Users\ssingh\RocketBuild_test'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'


def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        #repo.git.add(update=True)
        repo.git.add("test")
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')
    finally:
        print('Code push from script succeeded')


git_push()