# ulauncher-system-management-direct

[Ulauncher](https://ulauncher.io) extension allowing you to lock, suspend, reboot and shut down your system w/o an additional sub-menu.

![](screencast-demo.gif)


This extension is using experimental techniques to make Ulauncher keywords look and behave like apps. This comes with a couple of minor caveats but as of writing this, it works fine. These techniques were lifted from https://github.com/friday/ulauncher-gnome-settings

## How it works (primarily for extension developers)

This explanation was lifted directly from https://github.com/friday/ulauncher-gnome-settings and modified to apply to this extension

Ulauncher extensions can add multiple keywords, but not apps.

Keywords and apps have different workflows. Both have searchable names (like "Google Translate"), but triggering it will have different behavior. Triggering an app name will launch the app. Triggering the keyword name will replace your input with the keyword followed by a space, waiting for you to type an argument.

In addition to this, keywords can be typed directly. This skips the fuzzy search step.

To avoid the additional step and "launch" instead, this extension uses default keywords that look like names. That way if you select "Shut Down" it will replace your input with "Shut Down " (not something else like "shu "). This will show briefly before the KeywordQueryEvent-handler closes Ulauncher and runs the command. It looks a lot less hacky this way, and you may not even think about it.

Instead of spaces it's using an untypable blank character with the same width. Keywords can't contain spaces, since space is the separator between the keyword and the arguments. As a bonus, since it can't be typed with a keyboard it can only launch via search (like apps).

Users can override keywords in Ulauncher's preferences (hence the "default" in `default_value`). If you do this, this extension will not work as intended, but you may want to delete keywords completely if you don't want a specific panel to appear in search.

# Credits
- Originally forked from: https://github.com/friday/ulauncher-gnome-settings
  - Available under [MIT License](https://github.com/friday/ulauncher-gnome-settings/blob/v5/LICENSE)
- Icon courtesy of https://material.io/resources/icons
  - Available under [Apache license version 2.0](https://www.apache.org/licenses/LICENSE-2.0.html)
