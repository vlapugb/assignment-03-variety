# Задание #03. Всякое разное

## Правила

Задачи разбиваются на две категории:

- [`practice`](practice) &ndash; задания практики, частично разбираются на практике
- [`homework`](homework) &ndash; задания ДЗ для самостоятельного решения

Дедлайны и прочая инфа как обычно будет в Telegram канале.

Убедительная просьба писать код **самостоятельно**! Вы можете решать сложные задания вместе и обсуждать решения друг с
другом, но навык реализации своих идей в коде особо не разовьется от простого переписывания чужого кода.

Не редактируйте файлы в папке `.github`, а также файлы, заканчивающиеся на `_test.py`. Я все еще ленюсь написать скрипт,
который будет проверять, что они не изменены, но в целом мы сами увидим глазами на Review.

## Начальная настройка

### PyTest и pip

Если вы еще не установили `pytest` (интересно, почему), то вызовите следующую команду в терминале:

```shell
pip install pytest
```

Если он не может удачно установиться из-за прав доступа, замените на `pip install --user pytest`.

Если он при этом вывел надпись о том, что `pip` устарел, вызовите также после команду

```shell
python -m pip install --upgrade pip
```

### Репозиторий

Склонируйте этот репозиторий, если у него имя `assignment-03-variety-ваш-никнейм`.

Если у этого репозитория имя `assignment-03-variety`, вместо этого

- не клонируйте этот репозиторий
- не форкайте этот репозиторий
- вообще не трогайте этот репозиторий

Видите, как все просто :)

### Upstream

Репозиторий `assignment-03-variety` &ndash; это общий репозиторий, в котором у всех есть права на чтение и нет прав на
запись. Это означает, что с ним вы можете делать `git pull` (загрузить себе новые изменения), но не можете
делать `git push` (отправить свои изменения на GitHub).

В этот раз вы будете активно пользоваться опцией `git pull`, если нам понадобится внести некоторые изменения во ВСЕ ваши
репозитории (например, залить домашку). Для этого надо настроить доступ к общему репозиторию на чтение. В папке проекта
выполните следующую команду:

```shell
git remote add upstream git@github.com:ITMO-PhysTech-2021/assignment-03-variety.git
```

Теперь у вас есть два удаленных репозитория, с которыми вы можете работать:

- `origin` &ndash; ваш репозиторий, в который вы будете заружать свои решения
- `upstream` &ndash; общий репозиторий, из которого можно выгружать изменения, предназначенные для всех

Чтобы синхронизировать историю коммитов, сразу после этого выполните

```shell
git pull upstream
git reset --hard upstream/main
git push --force origin main
```

## Процесс выполнения заданий

Все условия находятся в файлах `_legend.md` в соответствующих папках `practice/TASKNAME` или `homework/TASKNAME`.

**Важно:** перед тестированием любого задания подгрузите изменения из общего репозитория:

```shell
git pull upstream main
```

### Практика

**Перейдите на ветку `practice`!**. Иначе ваши решения не будут автоматически тестироваться, и у вас есть шанс не
получить баллы.

```shell
git checkout -b practice
```

Протестировать задание можно запустив файл с тестами из PyCharm или запустив одну из следующих команд в терминале:

```shell
pytest practice/TASKNAME
python -m pytest practice/TASKNAME
```

Сделав какое-то задание, выполните команды, чтобы добавить изменения в Git, собрать их в один коммит и отправить на
GitHub:

```shell
git add practice/TASKNAME
git commit -m "practice TASKNAME finished"
git push origin practice
```

#### Pull Request

После того, как все задания практики сделаны, создайте Pull Request из ветки `practice` в ветку `main` и укажите своего
преподавателя в качестве Reviewer. **Не надо делать Merge** до того, как ваш код будет проверен преподавателем.

Pull Request можно сделать по ссылке, которая появляется, если вы делаете `git push origin practice`, либо в меню Pull Requests
на GitHub.

### Домашнее задание

**Перейдите на ветку `hw`!**. Иначе ваши решения не будут автоматически тестироваться, и у вас есть шанс не получить
баллы.

```shell
git checkout -b hw
```

Рекомендуется делать это после того, как сдана вся практика, и находясь на ветке `practice`. Если вы не завершили все
задания практики, но хотите начать делать ДЗ, ответвитесь от ветки `main`, как написано ниже. Заранее убедитесь, что у
вас нет незакоммиченных изменений.

```shell
git checkout -b hw main
```

Протестировать задание можно запустив файл с тестами из PyCharm или запустив одну из следующих команд в терминале:

```shell
pytest homework/TASKNAME
python -m pytest homework/TASKNAME
```

Сделав какое-то задание, выполните команды, чтобы добавить изменения в Git, собрать их в один коммит и отправить на
GitHub:

```shell
git add homework/TASKNAME
git commit -m "homework TASKNAME finished"
git push origin hw
```

#### Pull Request

Если вы сделали ДЗ, но еще не закончили задания практики,

1. сначала закончите задания практики, предварительно переключившись на ветку `practice` с
   помощью `git checkout practice`
2. вернитесь на ветку `hw` с помощью `git checkout hw`
3. переместите начало ветки `hw` на конец ветки `practice`:

```shell
git rebase --onto practice main
```

Если вы выполнили все предыдущие пункты, **делать PR отдельно для практики не надо**, просто сделайте PR из ветки `hw`,
как описано далее.

После того, как все задания ДЗ (и практики) сделаны, создайте Pull Request из ветки `hw` в ветку `main` и укажите своего
преподавателя в качестве Reviewer. **Не надо делать Merge** до того, как ваш код будет проверен преподавателем.

Pull Request можно сделать по ссылке, которая появляется, если вы делаете `git push origin hw`, либо в меню Pull Requests на
GitHub.