import git
from git_contributions_importer import *


repo = git.Repo(r"C:\Users\FP IT\Projects\Personal\alovega")
mock_repo = git.Repo(r"C:\Users\FP IT\Projects\helaplan-v3")

importer = Importer([repo], mock_repo)
importer.set_author(['alovegakevin@gmail.com','kevin.lugaziwa@financeplan.biz'])

importer.import_repository()