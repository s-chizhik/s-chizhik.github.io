Title: tricks.php
Date: 2017-01-27 10:20
Category: Статьи
Tags: php
Slug: tricks-php
Authors: Sergey Chizhik
Summary: Небольшой сборник различной странных вещей в php, с которыми приходилось столкнуться

Небольшой сборник различной странных вещей в php, с которыми приходилось столкнуться

-------

#### Вложенные тернарные операторы

    <?php

    $test = array();
    $test['a'] = 123;


    var_dump(
        isset($test['a'])
            ? $test['a']
            : isset($test['b'])
                ? $test['b']
                : "default"
    );


##### Ожидание
    <?php
    ...
    isset($test['a'])
        ? $test['a']
        : (isset($test['b'])
            ? $test['b']
            : "default")
    );

##### Реальность
    <?php
    ...
    (isset($test['a'])
        ? $test['a']
        : isset($test['b']))
            ? $test['b']
            : "default"
    );

-------

#### Вызов конструктора после создания объекта

    <?php
    ...
    $exception = new \Exception();
    var_dump($exception);

    $exception->__construct("Oups");
    var_dump($exception);

-------

#### Упоротый `in_array` ([документация](https://secure.php.net/manual/ru/function.in-array.php))

    <?php
    ...
    >>> in_array ("qwe", ["asd" => 0])
    => true

*Нужно учитывать, что `in_array` может принимать второй аргумент* 

-------

#### `sprintf` не работает с `mb_` строками


> Попытка использовать комбинацию строк и спецификаторов ширины с кодировками, которые > требуют более одного байта на символ, может привести к неожиданным результатам.

-------

#### Приаттачченый `callback` имеет доступ к `private` методам

-------
#### Symlinks && `is_dir`

    <?php

    $dir = '/tmp/symlink';
    if (is_dir($dir)) {
        rmdir($dir);
    }

`is_dir('/tmp/symlink')` читает что симлинк указывает на директорию, и `is_dir` отдаёт true, а `rmdir` не может удалить, т.к. фактически это симлинк.

*Актуально для 5 версии PHP*

-------
#### Вызов private метода внутри класса но не внутри себя, над другим объектом

    <?php

    class Test {
        
        private function privateFunction() {
            echo __METHOD__ . PHP_EOL;
        }
        
        protected function protectedFunction() {
            echo __METHOD__ . PHP_EOL;
        }
        
        public function publicFunction() {
            echo __METHOD__ . PHP_EOL;
        }
        
        public function doSomeStuf() {
            $newThis = clone $this;
            $newThis->publicFunction();
            $newThis->privateFunction();
            $newThis->protectedFunction();
        }
    }
    $a = new Test();
    $a->doSomeStuf();

-------

#### Смешанные аргументы в сигнатуре методов/функций:
    <?php
    ...
    function($a, $b = 0, $c) {
        var_dump($a, $b, $c);
    }

Аргументы со значениями по-умолчанию должны идти исключительно в конце, при нарушении – должна быть ошибка компиляции/процессинга и т.д

-------

#### (int) 18446744073709551615
    <?php
    >>> 18446744073709551615
    => 1.844674407371E+19

    >>> (int) 18446744073709551615
    => 0
