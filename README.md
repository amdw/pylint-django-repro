# pylint-django-repro

The purpose of this repository is to reproduce [a bug with pylint-django](https://github.com/PyCQA/pylint-django/issues/343).

Pre-requisites: Python 3 installation with pipenv.

Repro steps:

```shell
pipenv install --dev
pipenv shell
pylint --load-plugins=pylint_django --django-settings-module=repro.settings reproapp.views | grep no-member
```

Expected behaviour: no output, because the pylint-django plugin should recognise that the `objects` member exists.

Actual behaviour: prints the following line.

```
reproapp/views.py:5:11: E1101: Class 'MyModel' has no 'objects' member (no-member)
```

This seems to be caused by `astroid` 2.9.1. Proof:

```shell
pipenv install astroid==2.9.0
pylint --load-plugins=pylint_django --django-settings-module=repro.settings reproapp.views | grep no-member
```

This produces no output, as expected.

