<?php

// autoload_static.php @generated by Composer

namespace Composer\Autoload;

class ComposerStaticInit2f8e01d4c6458ef9dc926a29511dd8a7
{
    public static $files = array (
        'c964ee0ededf28c96ebd9db5099ef910' => __DIR__ . '/..' . '/guzzlehttp/promises/src/functions_include.php',
        'a0edc8309cc5e1d60e3047b5df6b7052' => __DIR__ . '/..' . '/guzzlehttp/psr7/src/functions_include.php',
        '37a3dc5111fe8f707ab4c132ef1dbc62' => __DIR__ . '/..' . '/guzzlehttp/guzzle/src/functions_include.php',
    );

    public static $prefixLengthsPsr4 = array (
        'P' => 
        array (
            'Psr\\Http\\Message\\' => 17,
        ),
        'G' => 
        array (
            'GuzzleHttp\\Psr7\\' => 16,
            'GuzzleHttp\\Promise\\' => 19,
            'GuzzleHttp\\' => 11,
        ),
    );

    public static $prefixDirsPsr4 = array (
        'Psr\\Http\\Message\\' => 
        array (
            0 => __DIR__ . '/..' . '/psr/http-message/src',
        ),
        'GuzzleHttp\\Psr7\\' => 
        array (
            0 => __DIR__ . '/..' . '/guzzlehttp/psr7/src',
        ),
        'GuzzleHttp\\Promise\\' => 
        array (
            0 => __DIR__ . '/..' . '/guzzlehttp/promises/src',
        ),
        'GuzzleHttp\\' => 
        array (
            0 => __DIR__ . '/..' . '/guzzlehttp/guzzle/src',
        ),
    );

    public static $classMap = array (
        'Tester\\Assert' => __DIR__ . '/..' . '/nette/tester/src/Framework/Assert.php',
        'Tester\\AssertException' => __DIR__ . '/..' . '/nette/tester/src/Framework/AssertException.php',
        'Tester\\CodeCoverage\\Collector' => __DIR__ . '/..' . '/nette/tester/src/CodeCoverage/Collector.php',
        'Tester\\CodeCoverage\\Generators\\AbstractGenerator' => __DIR__ . '/..' . '/nette/tester/src/CodeCoverage/Generators/AbstractGenerator.php',
        'Tester\\CodeCoverage\\Generators\\AcceptIterator' => __DIR__ . '/..' . '/nette/tester/src/CodeCoverage/Generators/AbstractGenerator.php',
        'Tester\\CodeCoverage\\Generators\\CloverXMLGenerator' => __DIR__ . '/..' . '/nette/tester/src/CodeCoverage/Generators/CloverXMLGenerator.php',
        'Tester\\CodeCoverage\\Generators\\HtmlGenerator' => __DIR__ . '/..' . '/nette/tester/src/CodeCoverage/Generators/HtmlGenerator.php',
        'Tester\\CodeCoverage\\PhpParser' => __DIR__ . '/..' . '/nette/tester/src/CodeCoverage/PhpParser.php',
        'Tester\\DataProvider' => __DIR__ . '/..' . '/nette/tester/src/Framework/DataProvider.php',
        'Tester\\DomQuery' => __DIR__ . '/..' . '/nette/tester/src/Framework/DomQuery.php',
        'Tester\\Dumper' => __DIR__ . '/..' . '/nette/tester/src/Framework/Dumper.php',
        'Tester\\Environment' => __DIR__ . '/..' . '/nette/tester/src/Framework/Environment.php',
        'Tester\\FileMock' => __DIR__ . '/..' . '/nette/tester/src/Framework/FileMock.php',
        'Tester\\Helpers' => __DIR__ . '/..' . '/nette/tester/src/Framework/Helpers.php',
        'Tester\\Runner\\CliTester' => __DIR__ . '/..' . '/nette/tester/src/Runner/CliTester.php',
        'Tester\\Runner\\CommandLine' => __DIR__ . '/..' . '/nette/tester/src/Runner/CommandLine.php',
        'Tester\\Runner\\HhvmPhpInterpreter' => __DIR__ . '/..' . '/nette/tester/src/Runner/HhvmPhpInterpreter.php',
        'Tester\\Runner\\Job' => __DIR__ . '/..' . '/nette/tester/src/Runner/Job.php',
        'Tester\\Runner\\OutputHandler' => __DIR__ . '/..' . '/nette/tester/src/Runner/OutputHandler.php',
        'Tester\\Runner\\Output\\ConsolePrinter' => __DIR__ . '/..' . '/nette/tester/src/Runner/Output/ConsolePrinter.php',
        'Tester\\Runner\\Output\\JUnitPrinter' => __DIR__ . '/..' . '/nette/tester/src/Runner/Output/JUnitPrinter.php',
        'Tester\\Runner\\Output\\Logger' => __DIR__ . '/..' . '/nette/tester/src/Runner/Output/Logger.php',
        'Tester\\Runner\\Output\\TapPrinter' => __DIR__ . '/..' . '/nette/tester/src/Runner/Output/TapPrinter.php',
        'Tester\\Runner\\PhpInterpreter' => __DIR__ . '/..' . '/nette/tester/src/Runner/PhpInterpreter.php',
        'Tester\\Runner\\Runner' => __DIR__ . '/..' . '/nette/tester/src/Runner/Runner.php',
        'Tester\\Runner\\TestHandler' => __DIR__ . '/..' . '/nette/tester/src/Runner/TestHandler.php',
        'Tester\\Runner\\ZendPhpDbgInterpreter' => __DIR__ . '/..' . '/nette/tester/src/Runner/ZendPhpDbgInterpreter.php',
        'Tester\\Runner\\ZendPhpInterpreter' => __DIR__ . '/..' . '/nette/tester/src/Runner/ZendPhpInterpreter.php',
        'Tester\\TestCase' => __DIR__ . '/..' . '/nette/tester/src/Framework/TestCase.php',
        'Tester\\TestCaseException' => __DIR__ . '/..' . '/nette/tester/src/Framework/TestCase.php',
    );

    public static function getInitializer(ClassLoader $loader)
    {
        return \Closure::bind(function () use ($loader) {
            $loader->prefixLengthsPsr4 = ComposerStaticInit2f8e01d4c6458ef9dc926a29511dd8a7::$prefixLengthsPsr4;
            $loader->prefixDirsPsr4 = ComposerStaticInit2f8e01d4c6458ef9dc926a29511dd8a7::$prefixDirsPsr4;
            $loader->classMap = ComposerStaticInit2f8e01d4c6458ef9dc926a29511dd8a7::$classMap;

        }, null, ClassLoader::class);
    }
}