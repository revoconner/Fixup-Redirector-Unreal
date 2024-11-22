#pragma once

#include "Runtime/Core/Public/CoreMinimal.h"
#include "Runtime/Engine/Classes/Kismet/BlueprintFunctionLibrary.h"
#include "RedirectorFixerBPLibrary.generated.h"

UCLASS()
class URedirectorFixerBPLibrary : public UBlueprintFunctionLibrary
{
    GENERATED_BODY()

public:
    UFUNCTION(BlueprintCallable, Category = "Redirector Fixer")
    static void FixupReferencers(const TArray<FString>& ObjectPaths);
};