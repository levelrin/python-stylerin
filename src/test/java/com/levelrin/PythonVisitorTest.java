package com.levelrin;

import com.levelrin.antlr.generated.PythonLexer;
import com.levelrin.antlr.generated.PythonParser;
import java.io.IOException;
import java.net.URISyntaxException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.CharStreams;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.tree.ParseTree;
import org.hamcrest.MatcherAssert;
import org.hamcrest.Matchers;
import org.junit.jupiter.api.Test;

final class PythonVisitorTest {

    /**
     * Assert that the formatter formats the code written in the `before` file that matches with the code written in the `after` file.
     *
     * @param before The file name that has code before formatting.
     * @param after The file name that has code after formatting.
     */
    void compare(final String before, final String after) {
        try {
            final Path beforePath = Paths.get(ClassLoader.getSystemResource(before).toURI());
            final String originalText = Files.readString(beforePath, StandardCharsets.UTF_8);
            final CharStream charStream = CharStreams.fromString(originalText);
            final PythonLexer lexer = new PythonLexer(charStream);
            final CommonTokenStream tokens = new CommonTokenStream(lexer);
            final PythonParser parser = new PythonParser(tokens);
            final ThrowableErrorListener errorListener = new ThrowableErrorListener();
            parser.removeErrorListeners();
            parser.addErrorListener(errorListener);
            final ParseTree tree = parser.file_input();
            final PythonVisitor visitor = new PythonVisitor(tokens);
            final String result = visitor.visit(tree);
            final Path afterPath = Paths.get(ClassLoader.getSystemResource(after).toURI());
            final String expectedText = Files.readString(afterPath, StandardCharsets.UTF_8);
            MatcherAssert.assertThat(
                String.format("Result:%n%s", result),
                result,
                Matchers.equalTo(expectedText)
            );
        } catch (final URISyntaxException | IOException ex) {
            throw new IllegalStateException(
                String.format(
                    "Failed to read files. before: %s, after: %s",
                    before,
                    after
                ),
                ex
            );
        }
    }

    @Test
    void shouldFormatSets() {
        this.compare("set-before.py", "set-after.py");
    }

    @Test
    void shouldFormatTuple() {
        this.compare("tuple-before.py", "tuple-after.py");
    }

    @Test
    void shouldFormatClass() {
        this.compare("class-before.py", "class-after.py");
    }

    @Test
    void shouldFormatComments() {
        this.compare("comment-before.py", "comment-after.py");
    }

    @Test
    void shouldFormatLambda() {
        this.compare("lambda-before.py", "lambda-after.py");
    }

    @Test
    void shouldFormatPassStatement() {
        this.compare("pass-before.py", "pass-after.py");
    }

    @Test
    void shouldFormatElseClauseInLoop() {
        this.compare("else-loop-before.py", "else-loop-after.py");
    }

    @Test
    void shouldFormatContinueAndBreakStatements() {
        this.compare("continue-break-before.py", "continue-break-after.py");
    }

    @Test
    void shouldFormatWhileLoop() {
        this.compare("while-before.py", "while-after.py");
    }

    @Test
    void shouldFormatIfStatements() {
        this.compare("if-before.py", "if-after.py");
    }

    @Test
    void shouldFormatForLoop() {
        this.compare("for-before.py", "for-after.py");
    }

    @Test
    void shouldFormatMain() {
        this.compare("main-before.py", "main-after.py");
    }

}
