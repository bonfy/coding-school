# Template

## 目的

Template + Data -> Document

## Function

New -> Parse -> Execute

## Loading Templates

* ParseFiles
* ParseGlob
* Lookup
* Must

## 模板嵌套

{{ define "_header.html" }}
{{ end }}

{{ template "_header.html" }}

## template composition

{{ block }}