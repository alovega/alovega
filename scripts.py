import git
from git_contributions_importer import *

repo = git.Repo(r"C:\Users\FP IT\Projects\Personal\dailyidea.com")
mock_repo = git.Repo(r"C:\Users\FP IT\Projects\Personal\alovega")

importer = Importer([repo], mock_repo)
importer.set_author(['alovegakevin@gmail.com','kevin.lugaziwa@financeplan.biz'])

importer.import_repository()