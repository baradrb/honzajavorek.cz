Title: Tahák na syntaxi: PHP VS. Java
Date: 2008-03-30 18:05:00
Tags: java, php

Ano, můžeme si otevřít knihy, můžeme zkoumat
[PHP syntaxi](http://en.wikipedia.org/wiki/PHP_syntax_and_semantics)
nebo [Java syntaxi](http://en.wikipedia.org/wiki/Java_syntax) na
Wikipedii, číst si v referenčních webech… Ale to je zdlouhavé.
Nabízím malý tahák pro stejně konvertované jako já – z PHP na Javu.
Nesnažil jsem se o nic komplexního, Javu se z toho nenaučíte. Jde
jen o výčet nejzákladnějších rozdílů v syntaxi, které se mohou
plést, zvláště když jsou zažité…

část syntaxe
PHP
Java
konstruktor
`__construct()`, `Class()`
`Class()`
toString
`$object->__toString()`
`object.toString()`
přístup ke statické proměnné/metodě
`Class::$name`, `Class::name()`
`Class.name`, `Class.name()`
přístup k vlastní statické proměnné/metodě
`self::$name`, `self::name()`
`name`, `Class.name`, `name()`, `Class.name()`
přístup k proměnné/metodě
`$object->name`, `$object->name()`
`object.name`, `object.name()`
přístup k vlastní proměnné/metodě
`$this->name`, `$this->name()`
`name`, `this.name`, `name()`, `this.name()`
(statická) konstanta
`const NAME`
`static final type NAME`
přístup ke konstantě
`self::NAME`, `Class::NAME`
`NAME`, `Class.NAME`
Mimochodem, když jsem hledal něco takového jako tento článek na
internetu, narazil jsem na
[pěkný tahák pro PHP](http://www.blueshoes.org/en/developer/php_cheat_sheet/).