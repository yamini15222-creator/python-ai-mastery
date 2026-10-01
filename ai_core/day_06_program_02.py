from dataclasses import dataclass


@dataclass
class DocumentChunk:
    document_name: str
    chunk_number: int
    content: str

    def preview(self, length: int = 50) -> str:
        return self.content[:length]


chunk = DocumentChunk(
    document_name="rag_notes.txt",
    chunk_number=1,
    content="RAG retrieves relevant document chunks before generating an answer.",
)

print(chunk)
print(chunk.preview())