import sys, getopt, re, os
from jinja2 import Environment, FileSystemLoader

def help():
  print("Usage: ")
  print("\tpython3 ./scripts/sync-deployment.py [-h|--help] [-a|--action <deploy|undeploy>] [-n|--network <network>] [-v|--version <version>]")



def main(argv):
  action = ''
  gitopsEnvironment = ''
  identityPool = ''
  version = '' 
  try:
    opts, args = getopt.getopt(argv,"ha:n:v:",["help","action=","network=","version="])
  except getopt.GetoptError:
    help()
    sys.exit(2)
  for opt, arg in opts:
    if opt in ('-h','--help'):
      help()
      sys.exit()
    elif opt in ("-a", "--action"):
      action = arg
    elif opt in ("-n", "--network"):
      network = arg
    elif opt in ("-v", "--version"):
      version = arg
  
  pr = re.sub('.*pr.','', version)
  applicationFile = f'./helm/pull-requests/templates/hoprd-node-{version}.yaml'
  if action == 'deploy':
    templateEnv = Environment(
      loader=FileSystemLoader("./scripts/", encoding='utf-8'),
      extensions=['jinja2_ansible_filters.AnsibleCoreFiltersExtension']
    )
    templateFile = templateEnv.get_template(f'pull-request-cluster-hoprd-{network}.yaml.j2')
    templateVariables = {
        'network': network,
        'version': version,
        'pr': pr
    }
    print(templateFile.render(templateVariables), file=open(applicationFile, 'w'))  
  else: # Undeploy
    os.remove(applicationFile)

if __name__ == "__main__":
   main(sys.argv[1:])
