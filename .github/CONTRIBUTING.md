# Contributing

Thank you for contributing to Lists of Information!

This repository serves as a curated collection of guides, notes, tools, services, and hardware references. The goal is to keep information consistent, easy to navigate, and simple to maintain.

If you would like documentation for something please submit an [issue](https://github.com/kevinthedang/lists-vault/issues)

## Adding New Content

1. Determine the appropriate category:

   - `services`
   - `tools`
   - `hardware`

2. Create a new Markdown file in the corresponding directory.

> [!NOTE]
> Sample File Structure
> lists-vault/
> ├── hardware/
> │   └── arduino.md
> ├── services/
> │   ├── fail2ban.md
> │   └── pi-hole.md
> ├── tools/
> │   └── java.md
> └── README.md

3. Use a descriptive file name (ex. `pi-hole.md` for PiHole)

> ![NOTE]
> Ensure the filename is always lowercase and uses hyphens

4. Header of the file should look like the following
```html
<div align="center">
	<p><a href="http/s link"><img alt="project-icon"
		src="../media/category/project"/></a></p>
	<h1>Title</h1>
  <h4>Short Description</h4>
</div>
```

> ![NOTE]
> Keep descriptions concise. For example for PiHole:
> DNS-based ad blocking and network-wide tracking protection."

5. Follow with main content and use clear headers
```md
## Overview

Provide a brief introduction.

## Installation (if applicable)

Provide installation steps.

## Configuration (if applicable)

Document any required configuration.

## Troubleshooting (if applicable)

## References

- Official Website
- GitHub Repository
- Documentation

...
```

> ![IMPORTANT]
> There is no need to edit `README.md` as it is auto-generated in Pull Requests prior to merging into the Default branch.
