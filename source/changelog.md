# Changelog

## v0.14.0

- Dynamically disable polling
- Basic support for [`pydantic`](https://pydantic-docs.helpmanual.io) models

[All changes since 0.13.0](https://github.com/adamghill/django-unicorn/compare/0.13.0...0.14.0).

## v0.13.0

- [Component key](components.md#component-key) to allow disambiguation of components of the same name
- [`$returnValue`](actions.md#returnvalue) special argument
- Get the last action method's [return value](actions.md#return-values)

[All changes since 0.12.0](https://github.com/adamghill/django-unicorn/compare/0.12.0...0.13.0).

## v0.12.0

- [Redirect](redirecting.md) from action method in component

[All changes since 0.11.2](https://github.com/adamghill/django-unicorn/compare/0.11.2...0.12.0).

## v0.11.2

- Fix encoding issue with default component template on Windows ([#91](https://github.com/adamghill/django-unicorn/issues/91))
- Fix circular import when creating the component ([#92](https://github.com/adamghill/django-unicorn/issues/92))

[All changes since 0.11.0](https://github.com/adamghill/django-unicorn/compare/0.11.0...0.11.2).

## v0.11.0

- [`$model`](actions.md#model) special argument and decorator.
- [`$toggle`](actions.md#toggle) special method.
- Support nested properties when using the [set shortcut](actions.md#set-shortcut).
- Fix action string arguments that would get spaces removed inadvertently.

**Breaking changes**

- All existing special methods now start with a `$` to signify they are magical. Therefore, `refresh` is now [`$refresh`](actions.md#refresh), `reset` is now [`$reset`](actions.md#reset), and `validate` is now [`$validate`](actions.md#validate).

[All changes since 0.10.1](https://github.com/adamghill/django-unicorn/compare/0.10.1...0.11.0).

## v0.10.1

- Use LRU cache for constructed components to prevent ever-expanding memory.
- Loosen `beautifulsoup4` version requirement.
- Fix bug to handle floats so that they don't lose precision when serialized to JSON.
- Fix bug to handle related models (ForeignKeys, OneToOne, etc) fields in Django models.

[All changes since 0.10.0](https://github.com/adamghill/django-unicorn/compare/0.10.0...0.10.1).

## v0.10.0

- Add support for [passing kwargs](components.md#component-arguments) into the component on the template
- Provide access to the [current request](advanced.md#request) in the component's methods

[All changes since 0.9.4](https://github.com/adamghill/django-unicorn/compare/0.9.4...0.10.0).

## v0.9.4

- Fix: Prevent Django `CharField` form field from stripping whitespaces when used for validation.
- Fix: Handle edge case that would generate a null exception.
- Fix: Only change loading state when an action method gets called, not on every event fire.

[All changes since 0.9.1](https://github.com/adamghill/django-unicorn/compare/0.9.1...0.9.3).

## v0.9.3

- Handle child elements triggering an event which should be handled by a parent unicorn element.

[All changes since 0.9.1](https://github.com/adamghill/django-unicorn/compare/0.9.1...0.9.3).

## v0.9.1

- Fix: certain actions weren't triggering model values to get set correctly

[All changes since 0.9.0](https://github.com/adamghill/django-unicorn/compare/0.9.0...0.9.1).

## v0.9.0

- [Loading states](loading-states.md) for improved UX.
- `$event` [special argument](actions.md#events) for `actions`.
- `u` [unicorn attribute](components.md#unicorn-attributes).
- `APPS` [setting](settings.md#apps) for determing where to look for components.
- Add support for parent elements for non-db models.
- Fix: Handle if `Meta` doesn't exist for db models.

[All changes since 0.8.0](https://github.com/adamghill/django-unicorn/compare/0.8.0...0.9.0).

## v0.8.0

- Add much more elaborate support for dealing with [Django models](django-models.md).

[All changes since 0.7.1](https://github.com/adamghill/django-unicorn/compare/0.7.1...0.8.0).

## v0.7.1

- Fix bug where multiple actions would trigger multiple payloads.
- Handle lazy models that are children of an action model better.

[All changes since 0.7.0](https://github.com/adamghill/django-unicorn/compare/0.7.0...0.7.1).

## v0.7.0

- Parse [action method arguments](actions.md#passing-arguments) as basic Python objects
- [Stop and prevent modifiers](actions.md#modifiers) on actions
- [Defer modifier](templates.md#defer) on model
- Support for multiple actions on the same element
- Django setting to [minimize](settings.md#minimize) the JavaScript

**Breaking changes**

- Remove unused `unicorn_styles` template tag
- Use dash for poll timing instead of dot

[All changes since 0.6.5](https://github.com/adamghill/django-unicorn/compare/0.6.5...0.7.0).

## v0.6.5

- Attempt to get the CSRF token from the cookie first before looking at the CSRF token.

[All changes since 0.6.4](https://github.com/adamghill/django-unicorn/compare/0.6.4...0.6.5).

## v0.6.4

- Fix bug where lazy models weren't sending values before an action was called
- Add `is_valid` method to component to more easily check if a component has validation errors.
- Better error message if the CSRF token is not available.

[All changes since 0.6.3](https://github.com/adamghill/django-unicorn/compare/0.6.3...0.6.4).

## v0.6.3

- Fix bug where model elements weren't getting updated values when an action was being called during the same component update.
- Fix bug where some action event listeners were duplicated.

[All changes since 0.6.2](https://github.com/adamghill/django-unicorn/compare/0.6.2...0.6.3).

## v0.6.2

- More robust fix for de-duping multiple actions.
- Fix bug where conditionally added actions didn't get an event listener.

[All changes since 0.6.1](https://github.com/adamghill/django-unicorn/compare/0.6.1...0.6.2).

## v0.6.1

- Fix model sync getting lost when there is an action ([issue 39](https://github.com/adamghill/django-unicorn/issues/39)).
- Small fix for validations.

[All changes since 0.6.0](https://github.com/adamghill/django-unicorn/compare/0.6.0...0.6.1).

## v0.6.0

- [Realtime validation](validation.md) of a Unicorn model.
- [Polling](polling.md) for component updates.
- [More component hooks](advanced.md)

[All changes since 0.5.0](https://github.com/adamghill/django-unicorn/compare/0.5.0...0.6.0).

## v0.5.0

- [Call](actions.md#calling-methods) component method from JavaScript.
- Support classes, dictionaries, Django Models, (read-only) Django QuerySets properties on a component.
- [Debounce](templates.md#debounce) modifier to change how fast changes are sent to the backend from `unicorn:model`.
- [Lazy](templates.md#lazy) modifier to listen for `blur` instead of `input` on `unicorn:model`.
- Better support for `textarea` HTML element.

[All changes since 0.4.0](https://github.com/adamghill/django-unicorn/compare/0.4.0...0.5.0).

## v0.4.0

- [Set shortcut](actions.md#set-shortcut) for setting properties.
- Listen for any valid event, not just `click`.
- Better handling for model updates when element ids aren't unique.

[All changes since 0.3.0](https://github.com/adamghill/django-unicorn/compare/0.3.0...0.4.0).

## v0.3.0

- Add [mount hook](advanced.md#mount).
- Add [reset](actions.md#reset) action.
- Remove lag when typing fast in a text input and overall improved performance.
- Better error handling for exceptional cases.

[All changes since 0.2.3](https://github.com/adamghill/django-unicorn/compare/0.2.3...0.3.0).

## v0.2.3

- Fix for creating default folders when running `startunicorn`.

[All changes since 0.2.2](https://github.com/adamghill/django-unicorn/compare/0.2.2...0.2.3).

## v0.2.2

- Set default `template_name` if it's missing in component.

[All changes since 0.2.1](https://github.com/adamghill/django-unicorn/compare/0.2.1...0.2.2).

## v0.2.1

- Fix `startunicorn` Django management command.

[All changes since 0.2.0](https://github.com/adamghill/django-unicorn/compare/0.2.0...0.2.1).

## v0.2.0

- Switch from `Component` class to `UnicornView` to follow the conventions of class-based views.
- [Investigate using class-based view instead of the custom Component class](https://github.com/adamghill/django-unicorn/issues/4)

[All changes since 0.1.1](https://github.com/adamghill/django-unicorn/compare/0.1.1...0.2.0).

## v0.1.1

- Fix package readme and repository link.

[All changes since 0.1.0](https://github.com/adamghill/django-unicorn/compare/0.1.0...0.1.1).

## v0.1.0

- Initial version with basic functionality.