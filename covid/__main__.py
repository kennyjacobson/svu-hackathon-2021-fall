import click

from covid import app


@click.command()
@click.option('-p','--param')

def run(param = 'foo'):
    if param == 'quicktest':
        print("quicktest was submitted as the parameter called param")
    else:
        df = app.summarize_data()

if __name__ == '__main__':
    #app.run()
    run()