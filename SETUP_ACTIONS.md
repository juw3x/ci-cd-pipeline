# Настройка GitHub Actions для CI/CD Pipeline

## Проблема: Нет галочки Actions

Если галочка "Actions" не появляется или workflows не запускаются, выполните следующие шаги:

## Шаг 1: Проверьте структуру файлов

Убедитесь, что workflow файлы находятся в правильном месте:

```
ci-cd-pipeline/
└── .github/
    └── workflows/
        ├── ci.yml
        └── cd.yml
```

## Шаг 2: Настройте GitHub Secrets

GitHub Actions требует секреты для доступа к Docker Hub:

### 2.1 Создайте Docker Hub аккаунт (если нет)
1. Зарегистрируйтесь на https://hub.docker.com/
2. Создайте Access Token:
   - Зайдите в Account Settings > Security > New Access Token
   - Дайте имя токену (например, "github-actions")
   - Выберите permissions: Read & Write
   - Сохраните токен (он появится только один раз!)

### 2.2 Добавьте Secrets в GitHub

1. Откройте репозиторий на GitHub: https://github.com/juw3x/ci-cd-pipeline
2. Перейдите в Settings > Secrets and variables > Actions
3. Нажмите "New repository secret"
4. Добавьте следующие секреты:

| Name | Secret | Description |
|------|--------|-------------|
| `DOCKER_USERNAME` | Ваше имя пользователя Docker Hub | Например: juw3x |
| `DOCKER_PASSWORD` | Ваш Docker Hub Access Token | Не пароль, а токен! |

## Шаг 3: Настройте Environments (для CD pipeline)

CD pipeline использует environments (staging и production):

1. Перейдите в Settings > Environments
2. Создайте environment "staging":
   - Name: `staging`
   - Environment URL: `https://staging.example.com` (можно оставить пустым для демо)
3. Создайте environment "production":
   - Name: `production`
   - Environment URL: `https://api.example.com` (можно оставить пустым для демо)
   - Включите "Required reviewers" если хотите добавить approval step

## Шаг 4: Активируйте GitHub Actions

1. Перейдите в вкладку "Actions" в репозитории
2. Если видите сообщение "GitHub Actions is currently disabled", нажмите "I understand my workflows, enable them"
3. GitHub Actions должен активироваться

## Шаг 5: Проверьте workflow

После активации workflows должны запуститься автоматически при следующем push:

### Для CI pipeline:
- Push в ветку `main` или `develop`
- Создание Pull Request в `main`

### Для CD pipeline:
- Push в ветку `main`
- Ручной запуск через Actions tab > "CD Pipeline" > "Run workflow"

## Шаг 6: Устранение неполадок

### Галочка Actions не появляется

**Причина 1**: Репозиторий пуст или нет .github/workflows/
- Решение: Убедитесь, что файлы ci.yml и cd.yml существуют в правильной директории

**Причина 2**: GitHub Actions отключен
- Решение: Settings > Actions > General > Enable GitHub Actions

**Причина 3**: Forked репозиторий
- Решение: В forked репозиториях Actions отключены по умолчанию.
  - Settings > Actions > General > Enable actions on forked repositories

### Workflows запускаются, но падают

**Ошибка: authentication failed**
- Проверьте DOCKER_USERNAME и DOCKER_PASSWORD secrets
- Убедитесь, что используете Access Token, а не пароль

**Ошибка: resource not accessible**
- Проверьте permissions у Docker Hub Access Token
- Токен должен иметь Read & Write permissions

**Ошибка: environment not found**
- Создайте environments staging и production в Settings > Environments

### CI работает, но CD не запускается

CD pipeline запускается только при push в main:
```bash
git checkout main
git merge feature-branch
git push origin main
```

Или вручную через Actions tab.

## Шаг 7: Быстрая проверка без Docker Hub

Если хотите протестировать только CI pipeline без Docker Hub:

Измените `.github/workflows/ci.yml` - уберите зависимость от CD или создайте отдельный тестовый workflow.

Или временно закомментируйте CD pipeline:
```bash
mv .github/workflows/ci.yml .github/workflows/ci.yml.disabled
git add .github/workflows/ci.yml.disabled
git commit -m "Temporarily disable CD"
git push
```

## Шаг 8: Проверка статуса

После push проверьте статус:

1. Откройте репозиторий на GitHub
2. Нажмите на вкладку "Actions"
3. Должны появиться workflow runs
4. Кликните на run для деталей

## Дополнительные ресурсы

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Docker Hub Access Tokens](https://docs.docker.com/security/for-developers/access-tokens/)
- [GitHub Environments](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment)

## Краткий чек-лист

- [ ] Workflow файлы в `.github/workflows/`
- [ ] GitHub Actions включён в Settings
- [ ] DOCKER_USERNAME secret добавлен
- [ ] DOCKER_PASSWORD secret добавлен (Access Token!)
- [ ] Environment "staging" создан
- [ ] Environment "production" создан
- [ ] Commit сделан и запушен в main
- [ ] Проверьте вкладку Actions для статуса

## Демо-режим (без реального деплоя)

Если хотите просто показать, что pipeline работает, без реального деплоя:

Оставьте workflow как есть - они будут работать, но деплой будет "фейковым" (просто echo команды). Это нормально для демонстрации.
